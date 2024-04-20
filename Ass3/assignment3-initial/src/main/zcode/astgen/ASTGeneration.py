from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        # return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])
        return Program(self.visit(ctx.declaration_list()))
    
    
    #### Declarations
    def visitDeclaration_list(self, ctx: ZCodeParser.Declaration_listContext):
        # return [self.visit(ctx.declaration())] + self.visit(ctx.declaration_list()) if ctx.declaration_list() else [self.visit(ctx.declaration())]
        return [self.visit(x) for x in ctx.declaration()]
    
    def visitDeclaration(self, ctx: ZCodeParser.DeclarationContext):
        return self.visit(ctx.getChild(0))
    
    # Var declaration
    def visitVariable_declaration(self, ctx: ZCodeParser.Variable_declarationContext):
        if ctx.parameter():
            var = self.visit(ctx.parameter())
            if ctx.expression():
                var.varInit = self.visit(ctx.expression())
            return var

        modifier = 'var' if ctx.VAR() else 'dynamic'
        varInit = self.visit(ctx.expression()) if ctx.expression() else None
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, modifier, varInit)
            
    
    # Function declaration
    def visitFunction_declaration(self, ctx: ZCodeParser.Function_declarationContext):
        param = self.visit(ctx.parameter_list()) # if ctx.parameter_list() else [] no need beause g4 let parameter_list empty (if can)
        body = self.visit(ctx.block_statement()) if ctx.block_statement() else self.visit(ctx.return_statement()) if ctx.return_statement() else None
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), param, body)
    
    # Parameter
    def visitParameter_list(self, ctx: ZCodeParser.Parameter_listContext):
        return [self.visit(ctx.parameter())] + self.visit(ctx.parameter_listtail()) if ctx.parameter() else []
    
    def visitParameter_listtail(self, ctx: ZCodeParser.Parameter_listtailContext):
        return [self.visit(ctx.parameter())] + self.visit(ctx.parameter_listtail()) if ctx.parameter() else []
    
    def visitParameter(self, ctx: ZCodeParser.ParameterContext):
        type = NumberType() if ctx.NUMBER() else StringType() if ctx.STRING() else BoolType()
        if ctx.number_list():
            type = ArrayType(self.visit(ctx.number_list()), type)
        # if ctx.number_list():
        #     if ctx.number_list().number_listtail().getChildCount() == 0:
        #         type = ArrayType(self.visit(ctx.number_list()), type)
        #         print("Array 1 demension")
        #     else:
        #         type = ArrayType(self.visit(ctx.number_list()), self.ArrayTypeDeclHelper(ctx.number_list().number_listtail(), type))
        #         print("Array multi demension")
                
        return VarDecl(Id(ctx.IDENTIFIER().getText()), type, None, None)
    
    # def ArrayTypeDeclHelper(self, ctx, type):
    #     if ctx.number_listtail().getChildCount() == 0:
    #         return type
    #     return ArrayType(self.visit(ctx), self.ArrayTypeDeclHelper(ctx.number_listtail(), type))
    
    # Number list for array
    def visitNumber_list(self, ctx: ZCodeParser.Number_listContext):
        return [float(ctx.NUMBER_LITERAL().getText())] + self.visit(ctx.number_listtail())
    
    def visitNumber_listtail(self, ctx: ZCodeParser.Number_listtailContext):
        return [float(ctx.NUMBER_LITERAL().getText())] + self.visit(ctx.number_listtail()) if ctx.NUMBER_LITERAL() else []
    
    
    #### Statements
    def visitStatement_list(self, ctx: ZCodeParser.Statement_listContext):
        # return [self.visit(ctx.statement())] + self.visit(ctx.statement_list()) if ctx.statement_list() else [self.visit(ctx.statement())]
        return [self.visit(x) for x in ctx.statement()]
    
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))
    
    # Assignment statement
    def visitAssignment_statement(self, ctx: ZCodeParser.Assignment_statementContext):
        lhs = ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression_list())) if ctx.expression_list() else Id(ctx.IDENTIFIER().getText())
        rhs = self.visit(ctx.expression())
        return Assign(lhs, rhs)
    
    # If statement
    def visitIf_statement(self, ctx: ZCodeParser.If_statementContext):
        expr, thenStmt = self.visit(ctx.if_part())
        elifStmt = self.visit(ctx.elif_list()) if ctx.elif_list() else []
        elseStmt = self.visit(ctx.else_part()) if ctx.else_part() else None
        return If(expr, thenStmt, elifStmt, elseStmt)
    
    def visitIf_part(self, ctx: ZCodeParser.If_partContext):
        return (self.visit(ctx.expression()), self.visit(ctx.statement()))
    
    def visitElif_list(self, ctx: ZCodeParser.Elif_listContext):
        # return [self.visit(ctx.elif_part())] + self.visit(ctx.elif_list()) if ctx.elif_list() else [self.visit(ctx.elif_part())]
        return [self.visit(x) for x in ctx.elif_part()]
    
    def visitElif_part(self, ctx: ZCodeParser.Elif_partContext):
        return (self.visit(ctx.expression()), self.visit(ctx.statement()))
    
    def visitElse_part(self, ctx: ZCodeParser.Else_partContext):
        return self.visit(ctx.statement())
    
    # For statement
    def visitFor_statement(self, ctx: ZCodeParser.For_statementContext):
        condExpr = self.visit(ctx.expression(0))
        updExpr = self.visit(ctx.expression(1))
        body = self.visit(ctx.statement())
        return For(Id(ctx.IDENTIFIER().getText()), condExpr, updExpr, body)
    
    # Break statement
    def visitBreak_statement(self, ctx: ZCodeParser.Break_statementContext):
        return Break()
    # Continue statement
    def visitContinue_statement(self, ctx: ZCodeParser.Continue_statementContext):
        return Continue()
    # Return statement
    def visitReturn_statement(self, ctx: ZCodeParser.Return_statementContext):
        return Return(self.visit(ctx.expression()) if ctx.expression() else None)
    # Function call statement
    def visitFunction_call_statement(self, ctx: ZCodeParser.Function_call_statementContext):
        callexpr = self.visit(ctx.function_call())
        return CallStmt(callexpr.name, callexpr.args)
    def visitFunction_call(self, ctx: ZCodeParser.Function_callContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression_list()) if ctx.expression_list() else [])
    # Block statement
    def visitBlock_statement(self, ctx: ZCodeParser.Block_statementContext):
        return Block(self.visit(ctx.statement_list()) if ctx.statement_list() else [])
    
    
    #### Expressions
    def visitExpression_list(self, ctx: ZCodeParser.Expression_listContext):
        return [self.visit(ctx.expression())] + self.visit(ctx.expression_listtail())
    
    def visitExpression_listtail(self, ctx: ZCodeParser.Expression_listtailContext):
        return [self.visit(ctx.expression())] + self.visit(ctx.expression_listtail()) if ctx.expression() else []
    
    def visitExpression(self, ctx: ZCodeParser.ExpressionContext):
        return self.visit(ctx.getChild(0))
    
    def visitString_operation(self, ctx: ZCodeParser.String_operationContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    
    def visitRelational_operation(self, ctx: ZCodeParser.Relational_operationContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    
    def visitLogical_operation(self, ctx: ZCodeParser.Logical_operationContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    
    def visitAdding_operation(self, ctx: ZCodeParser.Adding_operationContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    def visitMultiplying_operation(self, ctx: ZCodeParser.Multiplying_operationContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    
    def visitNot_operation(self, ctx: ZCodeParser.Not_operationContext):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        return self.visit(ctx.getChild(0))
    
    def visitSign_operation(self, ctx: ZCodeParser.Sign_operationContext):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        return self.visit(ctx.getChild(0))

    def visitElement(self, ctx: ZCodeParser.ElementContext):
        if ctx.getChildCount() == 4:
            if ctx.function_call():
                return ArrayCell(self.visit(ctx.function_call()), self.visit(ctx.expression_list()))
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expression_list()))
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.expression()) # subexpression
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        # function call or literal left
        return self.visit(ctx.getChild(0))
    
    #### Literals
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if ctx.NUMBER_LITERAL():
            return NumberLiteral(float(ctx.NUMBER_LITERAL().getText()))
        if ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText() == 'true')
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        
    def visitArray_literal(self, ctx: ZCodeParser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.expression_list()))