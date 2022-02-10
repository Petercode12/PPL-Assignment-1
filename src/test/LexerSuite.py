import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_1(self):
        self.assertTrue(TestLexer.test("katah_b234Dc","katah_b234Dc,<EOF>",1))

    def test_2(self):
        self.assertTrue(TestLexer.test("axx_C1245asda12Bbdc","axx_C1245asda12Bbdc,<EOF>",2))

    def test_3(self):
        self.assertTrue(TestLexer.test("_4A3e1212","_4A3e1212,<EOF>",3))

    def test_4(self):
        self.assertTrue(TestLexer.test("_BAD@boyz","_BAD,Error Token @",4))

    def test_5(self):
        self.assertTrue(TestLexer.test("$_212nme3 xoyz","$_212nme3,xoyz,<EOF>",5))

    def test_6(self):
        self.assertTrue(TestLexer.test("0132_3","01323,<EOF>",6))

    def test_7(self):
        self.assertTrue(TestLexer.test("0x8D_E_5","0x8DE5,<EOF>",7))

    def test_8(self):
        self.assertTrue(TestLexer.test("0B0111","0B0,111,<EOF>",8))

    def test_9(self):
        self.assertTrue(TestLexer.test("06218","0621,8,<EOF>",9))

    def test_10(self):
        self.assertTrue(TestLexer.test("0b135_163_5","0b1,351635,<EOF>",10))

    def test_11(self):
        self.assertTrue(TestLexer.test("13_42_","1342,_,<EOF>",11))

    def test_12(self):
       self.assertTrue(TestLexer.test("01120_13640B00","0112013640,B00,<EOF>",12))

    def test_13(self):
        self.assertTrue(TestLexer.test("0X00b000_eab","0X0,0b0,00,_eab,<EOF>",13))

    def test_14(self):
        self.assertTrue(TestLexer.test("0B1_011XA52","0B1011,XA52,<EOF>",14))

    def test_15(self):
        self.assertTrue(TestLexer.test("0X_FE2A12","0,X_FE2A12,<EOF>",15))

    def test_16(self):
        self.assertTrue(TestLexer.test(".47@1", ".,47,Error Token @", 16))

    def test_17(self):
        self.assertTrue(TestLexer.test(".453e+1", ".453e+1,<EOF>", 17))

    def test_18(self):
        self.assertTrue(TestLexer.test("25.", "25.,<EOF>", 18))

    def test_19(self):
        self.assertTrue(TestLexer.test("323334E+8542", "323334E+8542,<EOF>", 19))

    def test_20(self):
        self.assertTrue(TestLexer.test("23E.883", "23,E,.,883,<EOF>", 20))

    def test_21(self):
        self.assertTrue(TestLexer.test("14_4_8.0000","1448.0000,<EOF>",21))

    def test_22(self):
        self.assertTrue(TestLexer.test(".E0102040E+008",".E0102040,E,+,00,8,<EOF>",22))

    def test_23(self):
       self.assertTrue(TestLexer.test("2_8423.e-","28423.,e,-,<EOF>",23))

    def test_24(self):
        self.assertTrue(TestLexer.test("0101.00_00E-_123","0101,.,00,_00E,-,_123,<EOF>",24))

    def test_25(self):
        self.assertTrue(TestLexer.test("84_53_67_.493E+2_3","845367,_,.493E+2,_3,<EOF>",25))

    def test_26(self):
        self.assertTrue(TestLexer.test("False True True false False", "False,True,True,false,False,<EOF>", 26))

    def test_27(self):
        self.assertTrue(TestLexer.test("False _True", "False,_True,<EOF>", 27))

    def test_28(self):
        self.assertTrue(TestLexer.test(""" "cde\\k ac"  """, """Illegal Escape In String: cde\\k""", 28))

    def test_29(self):
        self.assertTrue(TestLexer.test(""" "abc '"12'"def """, """Unclosed String: abc '"12'"def """, 29))

    def test_30(self):
        self.assertTrue(TestLexer.test(""" "You are studying in \\\\ \\n UEH"  """, """You are studying in \\\\ \\n UEH,<EOF>""", 30))

    def test_31(self):
        self.assertTrue(TestLexer.test(""" "nuc11128\\f def"  """, """nuc11128\\f def,<EOF>""", 31))

    def test_32(self):
        self.assertTrue(TestLexer.test(""" "tkc' deg'f"  ""","""tkc' deg'f,<EOF>""",32))

    def test_33(self):
        self.assertTrue(TestLexer.test(""" "aofmbcd
        ghj" """, """Unclosed String: aofmbcd""", 33))

    def test_34(self):
        self.assertTrue(TestLexer.test(""" "A42888BC\\ "  """, """Illegal Escape In String: A42888BC\\ """, 34))

    def test_35(self):
        self.assertTrue(TestLexer.test(""" "unc\\n\\b tlg\\f\\r\\t ghj\\'\\\\" """, """unc\\n\\b tlg\\f\\r\\t ghj\\'\\\\,<EOF>""", 35))

    def test_36(self):
        self.assertTrue(TestLexer.test(""" "_Hello_worldtoday" ""","""_Hello_worldtoday,<EOF>""",36))

    def test_37(self):
        self.assertTrue(TestLexer.test(""" "We are coming soon '"@'" " ""","""We are coming soon '"@'" ,<EOF>""",37))

    def test_38(self):
        self.assertTrue(TestLexer.test(""" "\\\\ \\n hELasassLO evessalryofasne"  ""","""\\\\ \\n hELasassLO evessalryofasne,<EOF>""",38))

    def test_39(self):
        self.assertTrue(TestLexer.test(""" "OnTheEnd3m_4 ""","""Unclosed String: OnTheEnd3m_4 """,39))

    def test_40(self):
        self.assertTrue(TestLexer.test(""" "BKU is my luv\\\\ def"  """, """BKU is my luv\\\\ def,<EOF>""",40))

    def test_41(self):
        self.assertTrue(TestLexer.test(""" "3+40e-28*4\n"  """, """Unclosed String: 3+40e-28*4""",41))

    def test_42(self):
        self.assertTrue(TestLexer.test(""" "Array[Int,5]" """, """Array[Int,5],<EOF>""",42))

    def test_43(self):
        self.assertTrue(TestLexer.test(""" "14194\h'"5"  """, """Illegal Escape In String: 14194\h""",43))

    def test_44(self):
        self.assertTrue(TestLexer.test(""" "testeof\\\\n" """, """testeof\\\\n,<EOF>""",44))

    def test_45(self):
        self.assertTrue(TestLexer.test(""" "abfdasdlaksz" """, """abfdasdlaksz,<EOF>""",45))

    def test_46(self):
        self.assertTrue(TestLexer.test(""" PhuocPham"abdec\n xyz"  """, """PhuocPham,Unclosed String: abdec""",46))

    def test_47(self):
        self.assertTrue(TestLexer.test(""" "60Home "hello brother and sister" """, """60Home ,hello,brother,and,sister,Unclosed String:  """,47))

    def test_48(self):
        self.assertTrue(TestLexer.test(""" "BBQHello\\t" """, """BBQHello\\t,<EOF>""",48))

    def test_49(self):
        self.assertTrue(TestLexer.test(""" "##tONFsa\\n##" """, """##tONFsa\\n##,<EOF>""",49))

    def test_50(self):
        self.assertTrue(TestLexer.test(""" "0142+ntfrnyoyosao\\ def"  """, """Illegal Escape In String: 0142+ntfrnyoyosao\ """,50))

    def test_51(self):
        self.assertTrue(TestLexer.test("## Int main() {Class aram(){return 2;}}##_thisistheend","_thisistheend,<EOF>",51))

    def test_52(self):
        self.assertTrue(TestLexer.test("##okman##outofcmt######", "outofcmt,Error Token #", 52))

    def test_53(self):
        self.assertTrue(TestLexer.test("## *.+-\f\t ## ##", "Error Token #", 53))

    def test_54(self):
            self.assertTrue(TestLexer.test("note$#?#ef", "note,Error Token $", 54))

    def test_55(self):
        self.assertTrue(TestLexer.test("""## Class class: Puppy{
        Var
        x, y: Int = 50 % s, 3, 5;
        Var
        z: Float = 47 / 48;
        Val $c: Float = 2.E-5;
        $func()
        {
            Var
        f: String = "abc\\n";
        a = b;
        }

        ## ""","""<EOF>""",55))

    def test_56(self):
        self.assertTrue(TestLexer.test(""" Array("0+4 \\h") """, """Array,(,Illegal Escape In String: 0+4 \\h""",56))

    def test_57(self):
        self.assertTrue(TestLexer.test(""" Array(Array("EUH", "IUH","TTRAEE"),Array(1024,248,1665),Array(0b110101, 0x3EF,03456)) """, """Array,(,Array,(,EUH,,,IUH,,,TTRAEE,),,,Array,(,1024,,,248,,,1665,),,,Array,(,0b110101,,,0x3EF,,,03456,),),<EOF>""",57))

    def test_58(self):
        self.assertTrue(TestLexer.test("Var aof: Array[Float,12];", "Var,aof,:,Array,[,Float,,,12,],;,<EOF>", 58))

    def test_59(self):
        self.assertTrue(TestLexer.test("Val x, y: Array[Float,0xAFE];", "Val,x,,,y,:,Array,[,Float,,,0xAFE,],;,<EOF>", 59))

    def test_60(self):
        self.assertTrue(TestLexer.test("Bool x, y: Array[Float,0x0];", "Bool,x,,,y,:,Array,[,Float,,,0x0,],;,<EOF>", 60))

    def test_61(self):
        self.assertTrue(TestLexer.test("Val x, y: Array[Bool,10];", "Val,x,,,y,:,Array,[,Bool,,,10,],;,<EOF>", 61))

    def test_62(self):
        self.assertTrue(TestLexer.test("Array(212.589, 1289.3, 18.E-9, 61.7)", "Array,(,212.589,,,1289.3,,,18.E-9,,,61.7,),<EOF>", 62))

    def test_63(self):
        self.assertTrue(TestLexer.test(""" Array("\\\\a") """, """Array,(,\\\\a,),<EOF>""", 63))

    def test_64(self):
        self.assertTrue(TestLexer.test("Var a: Array = Array[String, -1];","Var,a,:,Array,=,Array,[,String,,,-,1,],;,<EOF>", 64))

    def test_65(self):
        self.assertTrue(TestLexer.test("Array(0b01011, 0X0, 0.e, 45NF)", "Array,(,0b0,1011,,,0X0,,,0.,e,,,45,NF,),<EOF>", 65))

    def test_66(self):
        self.assertTrue(TestLexer.test("obj_1st.obj_2nd::func(.e+1)", "obj_1st,.,obj_2nd,::,func,(,.e+1,),<EOF>", 68))

    def test_67(self):
        self.assertTrue(TestLexer.test("obj.attr[8] = 3", "obj,.,attr,[,8,],=,3,<EOF>", 67))

    def test_68(self):
        self.assertTrue(TestLexer.test("a<7 && b>9 || x == 18", "a,<,7,&&,b,>,9,||,x,==,18,<EOF>", 66))

    def test_69(self):
        self.assertTrue(TestLexer.test("+ * < - * / % == > > >= != < <= ", "+,*,<,-,*,/,%,==,>,>,>=,!=,<,<=,<EOF>", 74))

    def test_70(self):
        self.assertTrue(TestLexer.test("...ayohz", "..,.,ayohz,<EOF>", 70))

    def test_71(self):
        self.assertTrue(TestLexer.test(""" "We are CSE" +. ==. " Win" """, "We are CSE,+.,==., Win,<EOF>", 71))

    def test_72(self):
        self.assertTrue(TestLexer.test("self.obj = 620+457", "self,.,obj,=,620,+,457,<EOF>", 72))

    def test_73(self):
        self.assertTrue(TestLexer.test("! && || == !=", "!,&&,||,==,!=,<EOF>", 73))

    def test_74(self):
        self.assertTrue(TestLexer.test("""Calculate::$Shape(3.14,9,"Circle")""", """Calculate,::,$Shape,(,3.14,,,9,,,Circle,),<EOF>""", 74))

    def test_75(self):
        self.assertTrue(TestLexer.test("({[:::]})", "(,{,[,::,:,],},),<EOF>", 75))

        """test random"""
    def test_76(self):
        self.assertTrue(TestLexer.test("t += n/t-u*3", "t,+,=,n,/,t,-,u,*,3,<EOF>", 76))

    def test_77(self):
        self.assertTrue(TestLexer.test("a.b:c::d:e/k", "a,.,b,:,c,::,d,:,e,/,k,<EOF>", 77))

    def test_78(self):
        self.assertTrue(TestLexer.test("method testing ##Onthego##omg=", "method,testing,omg,=,<EOF>", 78))

    def test_79(self):
        self.assertTrue(TestLexer.test("0b_1120as1", "0,b_1120as1,<EOF>", 79))

    def test_80(self):
        self.assertTrue(TestLexer.test("0b000178", "0b0,00,178,<EOF>", 80))

    def test_81(self):
        self.assertTrue(TestLexer.test("0b011011", "0b0,11011,<EOF>", 81))

    def test_82(self):
        self.assertTrue(TestLexer.test("Var a : String;", "Var,a,:,String,;,<EOF>", 82))

    def test_83(self):
        self.assertTrue(TestLexer.test("$132_check_num", "$132_check_num,<EOF>", 83))

    def test_84(self):
        self.assertTrue(TestLexer.test("&&*()+-%&&$ohhnh", "&&,*,(,),+,-,%,&&,$ohhnh,<EOF>", 84))

    def test_85(self):
        self.assertTrue(TestLexer.test("0_Iam_h_o__t", "0,_Iam_h_o__t,<EOF>", 85))

    def test_86(self):
        self.assertTrue(TestLexer.test("$_deadline_coming", "$_deadline_coming,<EOF>", 86))

    def test_87(self):
        self.assertTrue(TestLexer.test("$_123?bc", "$_123,Error Token ?", 87))

    def test_88(self):
        self.assertTrue(TestLexer.test("next = New Obstacle()", "next,=,New,Obstacle,(,),<EOF>", 88))

    def test_89(self):
        self.assertTrue(TestLexer.test("@.@", "Error Token @", 89))

    def test_90(self):
        self.assertTrue(TestLexer.test("_._", "_,.,_,<EOF>", 90))

    def test_91(self):
        self.assertTrue(TestLexer.test("%$#@!%&", "%,Error Token $", 91))

    def test_92(self):
        self.assertTrue(TestLexer.test("0xAF123EDTN", "0xAF123ED,TN,<EOF>", 92))

    def test_93(self):
        self.assertTrue(TestLexer.test("(/-./+)", "(,/,-,.,/,+,),<EOF>", 93))

    def test_94(self):
        self.assertTrue(TestLexer.test("0x1_2__45F", "0x12,__45F,<EOF>", 94))

    def test_95(self):
        self.assertTrue(TestLexer.test("&&.)", "&&,.,),<EOF>", 95))

    def test_96(self):
        self.assertTrue(TestLexer.test("^.@", "Error Token ^", 96))

    def test_97(self):
        self.assertTrue(TestLexer.test("28.00000", "28.00000,<EOF>", 97))

    def test_98(self):
        self.assertTrue(TestLexer.test("+.*%", "+.,*,%,<EOF>", 98))

    def test_99(self):
        self.assertTrue(TestLexer.test(""" "This is nearly end \\n, okay" """, """This is nearly end \\n, okay,<EOF>""", 99))

    def test_100(self):
        self.assertTrue(TestLexer.test("#.#", "Error Token #", 100))
