# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrlit.
    def visitArrlit(self, ctx:D96Parser.ArrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mul_arrlit.
    def visitMul_arrlit(self, ctx:D96Parser.Mul_arrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprlist1.
    def visitExprlist1(self, ctx:D96Parser.Exprlist1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprlist2.
    def visitExprlist2(self, ctx:D96Parser.Exprlist2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr0.
    def visitExpr0(self, ctx:D96Parser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_list_1.
    def visitAttr_list_1(self, ctx:D96Parser.Attr_list_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_list_2.
    def visitAttr_list_2(self, ctx:D96Parser.Attr_list_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constdecl.
    def visitConstdecl(self, ctx:D96Parser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist1.
    def visitIdlist1(self, ctx:D96Parser.Idlist1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist2.
    def visitIdlist2(self, ctx:D96Parser.Idlist2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign.
    def visitAssign(self, ctx:D96Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifstmt.
    def visitIfstmt(self, ctx:D96Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockstmt.
    def visitBlockstmt(self, ctx:D96Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elifstmt.
    def visitElifstmt(self, ctx:D96Parser.ElifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elsestmt.
    def visitElsestmt(self, ctx:D96Parser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forstmt.
    def visitForstmt(self, ctx:D96Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#breakstmt.
    def visitBreakstmt(self, ctx:D96Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continuestmt.
    def visitContinuestmt(self, ctx:D96Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#returnstmt.
    def visitReturnstmt(self, ctx:D96Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_expr.
    def visitIndex_expr(self, ctx:D96Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operator.
    def visitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#accessor.
    def visitAccessor(self, ctx:D96Parser.AccessorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_create.
    def visitObject_create(self, ctx:D96Parser.Object_createContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_access.
    def visitAttr_access(self, ctx:D96Parser.Attr_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_access.
    def visitMethod_access(self, ctx:D96Parser.Method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_attr.
    def visitStatic_attr(self, ctx:D96Parser.Static_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method.
    def visitStatic_method(self, ctx:D96Parser.Static_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invoc.
    def visitMethod_invoc(self, ctx:D96Parser.Method_invocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecl.
    def visitClassdecl(self, ctx:D96Parser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_list_1_gen.
    def visitAttr_list_1_gen(self, ctx:D96Parser.Attr_list_1_genContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_list_2_gen.
    def visitAttr_list_2_gen(self, ctx:D96Parser.Attr_list_2_genContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl_general.
    def visitVardecl_general(self, ctx:D96Parser.Vardecl_generalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constdecl_general.
    def visitConstdecl_general(self, ctx:D96Parser.Constdecl_generalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist1_general.
    def visitIdlist1_general(self, ctx:D96Parser.Idlist1_generalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist2_general.
    def visitIdlist2_general(self, ctx:D96Parser.Idlist2_generalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paralist1.
    def visitParalist1(self, ctx:D96Parser.Paralist1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paralist2.
    def visitParalist2(self, ctx:D96Parser.Paralist2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#construct_decl.
    def visitConstruct_decl(self, ctx:D96Parser.Construct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destruct_decl.
    def visitDestruct_decl(self, ctx:D96Parser.Destruct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#declaration.
    def visitDeclaration(self, ctx:D96Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_decl.
    def visitArray_decl(self, ctx:D96Parser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dtype.
    def visitDtype(self, ctx:D96Parser.DtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dtype_array.
    def visitDtype_array(self, ctx:D96Parser.Dtype_arrayContext):
        return self.visitChildren(ctx)



del D96Parser