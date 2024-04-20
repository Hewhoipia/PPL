# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_list.
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_part.
    def visitIf_part(self, ctx:ZCodeParser.If_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_list.
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_part.
    def visitElif_part(self, ctx:ZCodeParser.Elif_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_part.
    def visitElse_part(self, ctx:ZCodeParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call.
    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration_list.
    def visitDeclaration_list(self, ctx:ZCodeParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration.
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_declaration.
    def visitVariable_declaration(self, ctx:ZCodeParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_declaration.
    def visitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_list.
    def visitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_listtail.
    def visitParameter_listtail(self, ctx:ZCodeParser.Parameter_listtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_list.
    def visitNumber_list(self, ctx:ZCodeParser.Number_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_listtail.
    def visitNumber_listtail(self, ctx:ZCodeParser.Number_listtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_list.
    def visitExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_listtail.
    def visitExpression_listtail(self, ctx:ZCodeParser.Expression_listtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_operation.
    def visitString_operation(self, ctx:ZCodeParser.String_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_operation.
    def visitRelational_operation(self, ctx:ZCodeParser.Relational_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_operation.
    def visitLogical_operation(self, ctx:ZCodeParser.Logical_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#adding_operation.
    def visitAdding_operation(self, ctx:ZCodeParser.Adding_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplying_operation.
    def visitMultiplying_operation(self, ctx:ZCodeParser.Multiplying_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#not_operation.
    def visitNot_operation(self, ctx:ZCodeParser.Not_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_operation.
    def visitSign_operation(self, ctx:ZCodeParser.Sign_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#element.
    def visitElement(self, ctx:ZCodeParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_literal.
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return self.visitChildren(ctx)



del ZCodeParser