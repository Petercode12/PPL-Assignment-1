import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_101(self):
        self.assertTrue(TestLexer.test("var","var,<EOF>",101))

    def test_102(self):
        self.assertTrue(TestLexer.test("1var","1,var,<EOF>",102))

    def test_103(self):
        self.assertTrue(TestLexer.test("_1var","_1var,<EOF>",103))

    def test_104(self):
        self.assertTrue(TestLexer.test("123_3a12","1233,a12,<EOF>",104))

    def test_105(self):
        self.assertTrue(TestLexer.test("#asdf##1sd_+##","Error Token #",105))

    def test_106(self):
        self.assertTrue(TestLexer.test("##as##","<EOF>",106))

    def test_107(self):
        self.assertTrue(TestLexer.test("##as##21_a", "21,_a,<EOF>", 107))

    def test_108(self):
        self.assertTrue(TestLexer.test("""3"##as##"21_a""", """3,"##as##",21,_a,<EOF>""", 108))

    def test_109(self):
        input = """ asdf$as12_32 123_32 """
        output = """asdf,$as12_32,12332,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 109))

    def test_110(self):
        input = """ "abc\\ha" """
        output = """Illegal Escape In String: abc\\h"""
        self.assertTrue(TestLexer.test(input, output, 110))

    def test_111(self):
        input = """ "abc\\\\ha" """
        output = """"abc\\\\ha",<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 111))

    def test_112(self):
        input = """ "abc\\\\" """
        output = """"abc\\\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 112))

    def test_113(self):
        input = """ "abc\\ """
        output = """Illegal Escape In String: abc\ """
        self.assertTrue(TestLexer.test(input, output, 113))

    def test_114(self):
        input = """## "ab\\##"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 114))

    def test_115(self):
        input = """123 456"""
        output = """123,456,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 115))

    def test_116(self):
        input = """12_3E1-32"""
        output = """123E1,-,32,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 116))

    def test_117(self):
        input = """12_3E1 _32E-1"""
        output = """123E1,_32E,-,1,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 117))

    def test_118(self):
        input = """12_3E1 _32E-1;4e-2"""
        output = """123E1,_32E,-,1,;,4e-2,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 118))

    def test_119(self):
        input = """12_3_3232E1_323_1"""
        output = """1233232E1,_323_1,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 119))

    def test_120(self):
        input = """12_3_32__32_E1_323_1"""
        output = """12332,__32_E1_323_1,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 120))

    def test_121(self):
        input = """1E-2-3,5"""
        output = """1E-2,-,3,,,5,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 121))

    def test_122(self):
        input = """1.3323a32"""
        output = """1.3323,a32,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 122))

    def test_123(self):
        input = """1.a12"""
        output = """1.,a12,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 123))

    def test_124(self):
        input = """1_323.e-1_23_4"""
        output = """1323.e-1,_23_4,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 124))

    def test_125(self):
        input = """.2abd"""
        output = """.,2,abd,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 125))

    def test_126(self):
        input = """1.2abd"""
        output = """1.2,abd,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 126))

    def test_127(self):
        input = """1.2e-2;1e3abd"""
        output = """1.2e-2,;,1e3,abd,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 127))

    def test_128(self):
        input = """0x1234e12"""
        output = """0x1234,e12,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 128))

    def test_129(self):
        input = """0x01234e12"""
        output = """0x0,1234e12,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 129))

    def test_130(self):
        input = """0b01234e12"""
        output = """0b0,1234e12,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 130))

    def test_131(self):
        input = """001234e12"""
        output = """00,1234e12,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 131))

    def test_132(self):
        input = """0127A334e12"""
        output = """0127,A334e12,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 132))

    def test_133(self):
        input = """0x12F3G_3,34e-2"""
        output = """0x12F3,G_3,,,34e-2,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 133))

    def test_134(self):
        input = """0x12F3G_3,34e-2"""
        output = """0x12F3,G_3,,,34e-2,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 134))

    def test_135(self):
        input = """trueTrue True"""
        output = """trueTrue,True,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 135))

    def test_136(self):
        input = """Falsefalse"""
        output = """Falsefalse,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 136))

    def test_137(self):
        input = """False false"""
        output = """False,false,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 137))

    def test_138(self):
        input = """ "strs\\rxc" """
        output = """"strs\\rxc",<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 138))

    def test_139(self):
        input = """ "'strs\\rxc" """
        output = """"'strs\\rxc",<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 139))

    def test_140(self):
        input=""" "He asked me: '"Where is John?'"" """
        output = """"He asked me: '\"Where is John?'\"",<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 140))

    def test_141(self):
        input=""" Array(1, 5, 20, -1) """
        output = """Array,(,1,,,5,,,20,,,-,1,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 141))

    def test_142(self):
        input=""" Array(1, 5, "str" , 20, -1) """
        output = """Array,(,1,,,5,,,"str",,,20,,,-,1,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 142))

    def test_143(self):
        input=""" Array(1e-12, "ab\\\\hc", "str") """
        output = """Array,(,1e-12,,,"ab\\\\hc",,,"str",),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 143))

    def test_144(self):
        input=""" Array(1e-12, "ab\\\\hc", "str) """
        output = """Array,(,1e-12,,,"ab\\\\hc",,,Unclosed String: str) """
        self.assertTrue(TestLexer.test(input, output, 144))

    def test_145(self):
        input = """ Array(
            Array("Attr 1", "1", 11),
            Array("Attr 2", "2", 2),
            Array("Attr 3", "3", 33),
        ) """
        output = """Array,(,Array,(,"Attr 1",,,"1",,,11,),,,Array,(,"Attr 2",,,"2",,,2,),,,Array,(,"Attr 3",,,"3",,,33,),,,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 145))

    def test_146(self):
        input = """ b = 12||!23 """
        output = """b,=,12,||,!,23,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 146))

    def test_147(self):
        input = """ b != 12||ds - 23! """
        output = """b,!=,12,||,ds,-,23,!,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 147))

    def test_148(self):
        input = """ Var var, c, d: Int = 3, 2"""
        output = """Var,var,,,c,,,d,:,Int,=,3,,,2,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 148))

    def test_149(self):
        input = """ Var var, c, d: Int = 3*b/2, 2+>=3, 5 <= 1"""
        output = """Var,var,,,c,,,d,:,Int,=,3,*,b,/,2,,,2,+,>=,3,,,5,<=,1,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 149))

    def test_150(self):
        input = """ Var str: String = "abc" +. "def" """
        output = """Var,str,:,String,=,"abc",+.,"def",<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 150))

    def test_151(self):
        input = """ Var arr: Array[Int, 6] """
        output = """Var,arr,:,Array,[,Int,,,6,],<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 151))

    def test_152(self):
        input = """ Var arr: Array[Array[Array[Float, 10], 6], 6] """
        output = """Var,arr,:,Array,[,Array,[,Array,[,Float,,,10,],,,6,],,,6,],<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 152))

    def test_153(self):
        input = """ Class Student: Person{
            main(){
                a = b;
            }
        }
        """
        output = """Class,Student,:,Person,{,main,(,),{,a,=,b,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 153))

    def test_154(self):
        input = """ Class Student: Person{
            Var a, b: Int = 2, 3;
            Val $c:Float = 1.e-3;
            $main(){
                a = b;
            }
        }
        """
        output = """Class,Student,:,Person,{,Var,a,,,b,:,Int,=,2,,,3,;,Val,$c,:,Float,=,1.e-3,;,$main,(,),{,a,=,b,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 154))

    def test_155(self):
        input = """
            Class Student: Person{
            Var a, b: Int = 2%s, 3;
            Var e: Float = 3/2;
            Val $c:Float = 1.e-3;
            $main(){
                Var f: String = "string";
                a = b;
            }
        }
        """
        output = """Class,Student,:,Person,{,Var,a,,,b,:,Int,=,2,%,s,,,3,;,Var,e,:,Float,=,3,/,2,;,Val,$c,:,Float,=,1.e-3,;,$main,(,),{,Var,f,:,String,=,"string",;,a,=,b,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 155))

    def test_156(self):
        input = """
            Class Student: Person{
            Var a, b: String = "str" +. c, "234!";
            $main(){
                Var f: String = "string" ==. "string2";
                a = b;
            }
        }
        """
        output = """Class,Student,:,Person,{,Var,a,,,b,:,String,=,"str",+.,c,,,"234!",;,$main,(,),{,Var,f,:,String,=,"string",==.,"string2",;,a,=,b,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 156))

    def test_157(self):
        input = """
            arr[2] = [1, 2, 3];
            arr[3][3] = 421;
        """
        output = """arr,[,2,],=,[,1,,,2,,,3,],;,arr,[,3,],[,3,],=,421,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 157))

    def test_158(self):
        input = """ arr[23-3/2*10 /2] = 46%2-65/2; """
        output = """arr,[,23,-,3,/,2,*,10,/,2,],=,46,%,2,-,65,/,2,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 158))

    def test_159(self):
        input = """
            ## Define class #Student ##
        """
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 159))

    def test_160(self):
        input = """ ### Define \\\\h class #Student ##"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 160))

    def test_161(self):
        input = """
            ### Define class #Student\\\\h ###

        """
        output = """Error Token #"""
        self.assertTrue(TestLexer.test(input, output, 161))

    def test_162(self):
        input = """
            ### _23450###9123\\->w32 ##

        """
        output = """Error Token #"""
        self.assertTrue(TestLexer.test(input, output, 162))

    def test_163(self):
        input = """
            ### 1---23 + 39.,2 32. 23e2/ a;s 234.//./2##

        """
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 163))

    def test_164(self):
        input = """12_32 __ 2341+1234"""
        output = """1232,__,2341,+,1234,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 164))

    def test_165(self):
        input = """b.c(12)"""
        output = """b,.,c,(,12,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 165))

    def test_166(self):
        input = """b.c(12)::foo"""
        output = """b,.,c,(,12,),::,foo,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 166))

    def test_167(self):
        input = """mn = b.c(12)::$foo(23_"""
        output = """mn,=,b,.,c,(,12,),::,$foo,(,23,_,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 167))

    def test_168(self):
        input = """stu.foo(12,3)::$mn(,.,.)"""
        output = """stu,.,foo,(,12,,,3,),::,$mn,(,,,.,,,.,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 168))

    def test_169(self):
        input = """tr.py(12).mn::$vjp = foo(12)::mn(123, 1)"""
        output = """tr,.,py,(,12,),.,mn,::,$vjp,=,foo,(,12,),::,mn,(,123,,,1,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 169))

    def test_170(self):
        input = """a.foo = mn - stu.foo(12,3)::$mn(,.,.)"""
        output = """a,.,foo,=,mn,-,stu,.,foo,(,12,,,3,),::,$mn,(,,,.,,,.,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 170))

    def test_171(self):
        input = """New Student(12, "name")"""
        output = """New,Student,(,12,,,"name",),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 171))

    def test_172(self):
        input = """Class Main(){}
            mainfunc = New Main();
        """
        output = """Class,Main,(,),{,},mainfunc,=,New,Main,(,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 172))

    def test_173(self):
        input = """<=.>=+.==.$%**//!!+<>>...!"""
        output = """<=,.,>=,+.,==.,Error Token $"""
        self.assertTrue(TestLexer.test(input, output, 173))

    def test_174(self):
        input = """<=.>=+.==.%**//!!+<>>...!"""
        output = """<=,.,>=,+.,==.,%,*,*,/,/,!,!,+,<,>,>,..,.,!,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 174))

    def test_175(self):
        input = """Self.selfie('haha')"""
        output = """Self,.,selfie,(,Error Token '"""
        self.assertTrue(TestLexer.test(input, output, 175))

    def test_176(self):
        input = """Self.me = Self.play("foik'"l")"""
        output = """Self,.,me,=,Self,.,play,(,"foik'"l",),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 176))

    def test_177(self):
        input = """Self.me % "easy'e" = Self.play("foik'"l")"""
        output = """Self,.,me,%,"easy'e",=,Self,.,play,(,"foik'"l",),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 177))

    def test_178(self):
        input = """0x123000b0120032"""
        output = """0x123000,b0120032,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 178))

    def test_179(self):
        input = """0x1230 00b01_2000x123__32"""
        output = """0x1230,00,b01_2000x123__32,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 179))

    def test_180(self):
        input = """0x1230 000b01_2000x123__32"""
        output = """0x1230,00,0b0,12000,x123__32,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 180))

    def test_181(self):
        input = """123________43 +++ 0x099120 / 000b01_200 0x123_32__"""
        output = """123,________43,+,+,+,0x0,99120,/,00,0b0,1200,0x12332,__,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 181))

    def test_182(self):
        input = """12324 % 2ckx +++ = b.foo(000b01_2000x123__32)"""
        output = """12324,%,2,ckx,+,+,+,=,b,.,foo,(,00,0b0,12000,x123__32,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 182))

    def test_183(self):
        input = """
            If (flag == 1) {b = c;}
            Else {b=a)
        """
        output = """If,(,flag,==,1,),{,b,=,c,;,},Else,{,b,=,a,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 183))

    def test_184(self):
        input = """
            If (flag == 1) {b = c;}
            Elseif (flag == 0) {
                as = mn;
                as.boo("hehe");
            }
            Else {
                Var c: Int = 123 * 12/23;
            }
        """
        output = """If,(,flag,==,1,),{,b,=,c,;,},Else,{,b,=,a,),<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 184))

    def test_184(self):
        input = """
            If (count == 2) {b = c;}
            Elseif (count == 4) {
               $ks = kh();
            }
            Else {
                Var d: Float = 123e-10 * 12/23;
            }
        """
        output = """If,(,count,==,2,),{,b,=,c,;,},Elseif,(,count,==,4,),{,$ks,=,kh,(,),;,},Else,{,Var,d,:,Float,=,123e-10,*,12,/,23,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 184))

    def test_185(self):
        input = """
            Foreach(ab In 12 .. 34){}
        """
        output = """Foreach,(,ab,In,12,..,34,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 185))

    def test_186(self):
        input = """
            Foreach(ab In 12 .. 34 By 2){
                a.go().bro();
            }
        """
        output = """Foreach,(,ab,In,12,..,34,By,2,),{,a,.,go,(,),.,bro,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 186))

    def test_187(self):
        input = """
            Foreach(ab In 212 .. 34 By -12){
                If (break == 1) {
                    Break;
                }
                Else { go(); }
            }
        """
        output = """Foreach,(,ab,In,212,..,34,By,-,12,),{,If,(,break,==,1,),{,Break,;,},Else,{,go,(,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 187))

    def test_188(self):
        input = """
            Foreach(ab In 12 .. 34 By 2){
                mn = youtube;
                let().go(var + 123 /12);
            }
        """
        output = """Foreach,(,ab,In,12,..,34,By,2,),{,mn,=,youtube,;,let,(,),.,go,(,var,+,123,/,12,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 188))

    def test_189(self):
        input = """
            Foreach(m In 12.2 .. 123.4 By 1){
                Return False;
            }
        """
        output = """Foreach,(,m,In,12.2,..,123.4,By,1,),{,Return,False,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 189))

    def test_190(self):
        input = """
            Foreach(m In 12.2 .. 123.4 By 1){
                Return False;
            }
        """
        output = """Foreach,(,m,In,12.2,..,123.4,By,1,),{,Return,False,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 190))

    def test_191(self):
        input = """
            If (c == 2) {de = c/2341*123;}
            Elseif (count == 4) {
               Foreach(m In 12.2 .. 123.4 By 1){
                    Return False;
            }
            }
            Else {
                Var d: Float = 123e-10 * 12/23;
            }
        """
        output = """If,(,c,==,2,),{,de,=,c,/,2341,*,123,;,},Elseif,(,count,==,4,),{,Foreach,(,m,In,12.2,..,123.4,By,1,),{,Return,False,;,},},Else,{,Var,d,:,Float,=,123e-10,*,12,/,23,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 191))

    def test_192(self):
        input = """
            If (c == 2.....234<<<21321) {de = c/2341****++++123;}
            Elseif (count == 4) {
                Var a: Int = 12;
                Foreach(m good munia In 12.2 .. 123.4 By 1){
                    Return False;
            }
        """
        output = """If,(,c,==,2.,..,..,234,<,<,<,21321,),{,de,=,c,/,2341,*,*,*,*,+,+,+,+,123,;,},Elseif,(,count,==,4,),{,Var,a,:,Int,=,12,;,Foreach,(,m,good,munia,In,12.2,..,123.4,By,1,),{,Return,False,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 192))

    def test_193(self):
        input = """
            If (c == 2.....234<<<21321) {de = c/2341****++++123;}
            Elseif (count == 4) {
                Var a: Int = 12;
                Foreach(m good munia In 12.2 .. 123.4 By 1){
                    Return False;
            }
        """
        output = """If,(,c,==,2.,..,..,234,<,<,<,21321,),{,de,=,c,/,2341,*,*,*,*,+,+,+,+,123,;,},Elseif,(,count,==,4,),{,Var,a,:,Int,=,12,;,Foreach,(,m,good,munia,In,12.2,..,123.4,By,1,),{,Return,False,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 193))

    def test_194(self):
        input = """
            If (c == 2.....234<<<21321) {
                If (flag == 1) {b = c;}
                Elseif (flag == 2) {gud = mn * 923 / 123;}
                Else {b=a}
                de = c/2341****++++123;
            }
            Else {
                Var a: Int = 12;
                Foreach(m good munia In 12.2 .. 123.4 By 1){
                    Return False;
            }
        """
        output = """If,(,c,==,2.,..,..,234,<,<,<,21321,),{,If,(,flag,==,1,),{,b,=,c,;,},Elseif,(,flag,==,2,),{,gud,=,mn,*,923,/,123,;,},Else,{,b,=,a,},de,=,c,/,2341,*,*,*,*,+,+,+,+,123,;,},Else,{,Var,a,:,Int,=,12,;,Foreach,(,m,good,munia,In,12.2,..,123.4,By,1,),{,Return,False,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 194))

    def test_195(self):
        input = """
            If (c == 2.....234<<<21321) {
                If (flag == 1) {b = c;}
                Elseif (flag == 2) {gud = mn * 923 / 123;}
                Else {b=a}
                de = c/2341****++++123;
            }
            Else {
                Var a: Int = 12;
                Foreach(m good munia In 12.2 .. 123.4 By 1){
                    Foreach(m good munia In 12.2 .. 123.4 By 1){
                        Break;
                    }
                    Return False;
                }
            }
        """
        output = """If,(,c,==,2.,..,..,234,<,<,<,21321,),{,If,(,flag,==,1,),{,b,=,c,;,},Elseif,(,flag,==,2,),{,gud,=,mn,*,923,/,123,;,},Else,{,b,=,a,},de,=,c,/,2341,*,*,*,*,+,+,+,+,123,;,},Else,{,Var,a,:,Int,=,12,;,Foreach,(,m,good,munia,In,12.2,..,123.4,By,1,),{,Foreach,(,m,good,munia,In,12.2,..,123.4,By,1,),{,Break,;,},Return,False,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 195))

    def test_196(self):
        input = """
            If (c == 2.....234<<<21321) {
                If (flag == 1) {b = c;}

                    }
                    Return False;
                }
            }
        """
        output = """If,(,c,==,2.,..,..,234,<,<,<,21321,),{,If,(,flag,==,1,),{,b,=,c,;,},},Return,False,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 196))

    def test_197(self):
        input = """
            Foreach(m In 123.2 .. 1.4 By -2.3){
                If (True) {}
                Elseif (flag == 4) {gud = mn * 0x12 / 34%2342;}
                Else {b=a;
                    If (flag == 12) {b = c;}
                    Elseif (flag == 0) {
                        as = mn & 23;
                        as.boo("hehe");

            }
        """
        output = """Foreach,(,m,In,123.2,..,1.4,By,-,2.3,),{,If,(,True,),{,},Elseif,(,flag,==,4,),{,gud,=,mn,*,0x12,/,34,%,2342,;,},Else,{,b,=,a,;,If,(,flag,==,12,),{,b,=,c,;,},Elseif,(,flag,==,0,),{,as,=,mn,Error Token &"""
        self.assertTrue(TestLexer.test(input, output, 197))

    def test_198(self):
        input = """
            Else {
                Var a: Int = 12;
                Foreach(m good munia In 12.2 .. 123.4 By 1){
                    Foreach(m good munia In 12.2 .. 123.4 By 1){
                        Break;
                    }
                    Return False;
                }
            }
        """
        output = """Else,{,Var,a,:,Int,=,12,;,Foreach,(,m,good,munia,In,12.2,..,123.4,By,1,),{,Foreach,(,m,good,munia,In,12.2,..,123.4,By,1,),{,Break,;,},Return,False,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 198))

    def test_199(self):
        input = """
            If (flag == 1) {b = c;}
                Elseif (flag == 2) {gud = mn * 923 / 123;}
                Else {b=a}
                de = c/2341****++++123;
        """
        output = """If,(,flag,==,1,),{,b,=,c,;,},Elseif,(,flag,==,2,),{,gud,=,mn,*,923,/,123,;,},Else,{,b,=,a,},de,=,c,/,2341,*,*,*,*,+,+,+,+,123,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 199))

    def test_200(self):
        input = """
            If (c == 2.....234<<<21321) {
                If (flag == 1) {b = c;
                    Foreach(m In 12.2 .. 123.4 By 1.3){
                        If (True) {}
                        Elseif (flag == 2) {gud = mn * 923 / 123;}
                        Else {b=a}
                        Continue;
                    }
                }
                de = c/2341****++++123;
            }
        """
        output = """If,(,c,==,2.,..,..,234,<,<,<,21321,),{,If,(,flag,==,1,),{,b,=,c,;,Foreach,(,m,In,12.2,..,123.4,By,1.3,),{,If,(,True,),{,},Elseif,(,flag,==,2,),{,gud,=,mn,*,923,/,123,;,},Else,{,b,=,a,},Continue,;,},},de,=,c,/,2341,*,*,*,*,+,+,+,+,123,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 200))