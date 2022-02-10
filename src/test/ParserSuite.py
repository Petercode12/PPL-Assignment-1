import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    """ Test class declaration """

    def test_201(self):
        """Simple program: int main() {} """
        input = """Class main{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        input = """
        Class StudentA: Shape {
            getFinalScore() {
            Return self.midterm + self.final;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        input = """Var a: Array;"""
        expect = "Error on line 1 col 0: Var"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        input = """2+3+4"""
        expect = "Error on line 1 col 0: 2"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        input = """
        Class Shape {
            $_getNum{
                Return 1+2;
            }
        }
        """
        expect = "Error on line 3 col 20: {"
        self.assertTrue(TestParser.test(input, expect, 205))

    """ Test attribute declaration """

    def test_206(self):
        input = """
                Class Shape {
                   Var Area,$pi : Int = 12*3, 3.14;
                   Val $pos,$sigma: Array[Float,4];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        input = """
            Class Shape {
                Var x, y: Float = 2.5,7.6,12.8;
            }
            """
        expect = "Error on line 3 col 41: ,"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        input = """
                Class Position{
                    Var x, y: Float;
                }

                Class Shape {
                    Var note: String = "Rectangle \\n Square";
                    Val $pos,$sigma: Array[Position,2];
                }
                """
        expect = "Error on line 8 col 43: Position"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        input = """
                Class Shape {
                    Var Area :Array[Array[String,2],2] = Array(Array("Height","Length"),Array("Pi","Width"));
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        input = """
            Class Shape {
                Var arr: Array[Int,1];
                Val arr2: Array[Int,-1];
            }
            """
        expect = "Error on line 4 col 36: -"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        """More complex program"""
        input = """
            Class Shape {
                Var arr: Array[Int,-1];
            }
            """
        expect = "Error on line 3 col 35: -"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        Class Rectangle: Shape {
            getArea() {
                Return self.length * self.width;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = "Error on line 7 col 23: $numOfShape"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        input = """
        Class Shape {
            Constructor(width, height : Int; name:String){
                Self.Area=Self.width*Self.height;
                Self.name="shape"+.name;
            } 
            Destructor(){} 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        input = """
        Class Shape {
            foo(){
                a=1-------2+3*4/2;
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        input = """
        Class Culture{
            foo(){
                country = New a().b();
            } 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    """ Test method declaration """

    def test_216(self):
        input = """
            Class Shape {
                Rectangle(){
                    Area();
                } 
            }
            """
        expect = "Error on line 4 col 24: ("
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        input = """
            Class Program {
                main(){
                    a::$b.c.foo();
                    Var d: Int = 5;
                } 
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        """More complex program"""

        input = """
                Class Shape {
                    Area(){
                        k = 5;
                        Var $r, s: Int;
                    } 
                }
            """
        expect = "Error on line 5 col 28: $r"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):
        input = """
            Class Shape {
                foo(){
                    Var a, b: Array[Int, 5] = Array(1,2,3,4,5), Array(6,7,8,9,10);
                } 
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):
        """More complex program"""
        input = """
            Class Shape {
                Area(){
                    b.c.d.e = 5 + 4;
                    a::$b = c.d.e;
                } 
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        input = """
            Class _class_{
                Constructor(){

                };
                foo(){
                    country = New X().Y();
                } 
            }
            """
        expect = "Error on line 5 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        input = """
            Class _class_{
            Destructor(){
                Return;
            }
            foo(){
                country = New X().Y();
            } 
        }

            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        input = """
            Class _class_{
            Destructor(a,c: Int; b : Float){
                Return;
            }
        }
            """
        expect = "Error on line 3 col 23: a"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        input = """
            Class _class_ {
           foo(){
                a = !!!!!!!!True || False;
                b = ---4 + 3;
           }  
           Constructor(a,c: Bool; b : Float){
                Return a+b-c;
           }
        }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        input = """
            Class _bku_ {
                foo(){
                    a = !!!!!!True && !!!False;
                    b = ----5;
                    c=d::$e.d.d;
                    e=f[1+1][1][1][1];
                } 
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        input = """
            Class _bku_ {
                foo(){
                    a = (b==c) == True;
                } 
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        input = """
            Class _bku_{
                $foo(){
                    bku.$f = b == c  == True;
                } 
            }
            """
        expect = "Error on line 4 col 24: $f"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        input = """
            Class _bku_{
                $foo(){
                    a = b < c < True;
                } 
            }
            """
        expect = "Error on line 4 col 30: <"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        input = """
            Class _bku_{
            Var a: Float;
                $foo(){
                    a = ("here come the " +. " goat") +. "s";
                    c = ("a"==."a")==True;
                } 
            }

            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_230(self):
        input = """
            Class _bku_{
            foo(){
                    foo(){
                };
            }
        }
            """
        expect = "Error on line 4 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 230))

    """ Test expression """

    def test_231(self):
        input = """
                Class Phuoc{
                    Check_expr(){
                        x = New X();
                        x = a + b*c[5];
                        Return x; 
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        input = """
            Class _bku_{
                foo(){
                    a = 3 + 4 - (-2 / -3) ; 
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        input = """
            Class Phuoc{
                Check_expr(){
                    Var x: Array[Array[Float,5],2];
                    x = Array(Array(2.5e+1,4.6,3.2*5.1+2.2,4.3,8.2*3 - 1.e1), Array(46e2,53.00+1,4.5/5,2.*3.2,3.2-5.0));
                    Return x; 
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        input = """
            Class Phuoc{
                Check_expr(){
                    Var x: Array[Array[String,2],2];
                    x = Array(Array("Hello world", "abc" +. "def"), Array("Oke, let's check \\n here", "It's okay"));
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        input = """
            Class Phuoc{
                Check_expr(){
                    Var x: Array[Array[String,2],-1];
                    x = Array(Array("Hello world", "abc" +. "def"), Array("Oke, let's check \\n here", "It's okay"));
                }
            }
            """
        expect = "Error on line 4 col 49: -"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        input = """
            Class Phuoc{
                Val $b: Int = 5*3-1;
                Check_expr(){
                    Var a: Bool = !1 && 1 || 0 && (1+1); 
                    Val c: X = New X();
                    Var d: Int;
                    d = c::$b.e + 23*4/5%6;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        input = """
            Class Phuoc {
                foo(){
                    Var a: Bool;
                    a = 2 > 5 == 4 <= 6 < (! 5) >= (-2 + 8);
                } 
            }
        """
        expect = "Error on line 5 col 30: =="
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        input = """
                Class Phuoc {
                    foo(){
                        Var a: Bool;
                        a = 2 > 6 ! 5 >= (-2 + 8);
                    } 
                }
                """
        expect = "Error on line 5 col 34: !"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        input = """
        Class _bku_{
            Var a, b: Int = 3%7, -2;
            Var e: Float = 3/2;
            Val $c: Float = 0.e+000 - -3;

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        input = """
        Class _bku_ {
            foo(){
                Var $a :Int = 1;
            } 
        }
        """
        expect = "Error on line 4 col 20: $a"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = """
                    Class Phuoc{
                        foo(){
                            Var a: Array[Int, 01];
                            Var b: Array[Int, 0x1];
                            Var c: Array[Int, 0X1];
                            Var d: Array[Int, 0b1];
                            Var e: Array[Int, 0B1];
                            Val f: Array[Int, 1];
                            Val g: Array[Int, 07];
                            Val h: Array[Int, 0b0];
                        }
                    }

                """
        output = """Error on line 11 col 46: 0b0"""
        self.assertTrue(TestParser.test(input, output, 241))

    def test_242(self):
        input = """
                Class Phuoc{
                    foo(){
                        Var a, b: Float;
                        object.a.attr = Self.c*8 + b;
                    }
                }
            """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 242))

    def test_243(self):
        input = """
                Class Phuoc{
                    foo(){
                        a = 1;
                        a.func() = 5;
                    }
                }
            """
        output = """Error on line 5 col 33: ="""
        self.assertTrue(TestParser.test(input, output, 243))

    def test_244(self):
        input = """
                Class Phuoc{
                    Var a: Int;
                    Class Shape2{}
                }
            """
        output = """Error on line 4 col 20: Class"""
        self.assertTrue(TestParser.test(input, output, 244))

    def test_245(self):
        input = """
            Class Phuoc{
                foo(){
                    Var x, y: XY;
                    x = New XY();
                    y = New XY();
                    z = x + y;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 245))

    def test_246(self):
        input = """
            Class _bku_{
                foo(){
                    Var a: Array[Int, -1];
                }
            }
        """
        output = """Error on line 4 col 38: -"""
        self.assertTrue(TestParser.test(input, output, 246))

    def test_247(self):
        input = """
            Class _bku_{
                foo(){
                    Var a: Array[Int, 5];
                    a = Array(1,2,-1,3,4,5) + Array(4,3,2,1,0) == 1;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 247))

    def test_248(self):
        input = """
            Class _bku_{
                foo(){
                    Var a: Int = a+.( b ==. c) || !d[1] % e.f + -g::$h >= 1;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 248))

    def test_249(self):
        input = """
            Class _bku_{
                func(){
                    Var a: Array[Int, 1_23.456e+7];
                }
            }
        """
        output = """Error on line 4 col 38: 123.456e+7"""
        self.assertTrue(TestParser.test(input, output, 249))

    def test_250(self):
        input = """
            Class _bku_ {
            foo(){
                Var a : Array[Float, b::$f0];
                } 
            }
        """
        output = """Error on line 4 col 37: b"""
        self.assertTrue(TestParser.test(input, output, 250))



    def test_251(self):
        input = """
        Class _bku_
        {
            foo()
        {
            Var
        a: Array[Int, 1] = Array(1);
        a = Array(1, 2, -1, 3, 4, 5) + Array(4, 3, 2, 1, 0) == 1;
        }
        }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 251))

    def test_252(self):
        input = """
            Class _bku_{
            Var $arr : Array[Int,3], Array[Int,2];
            }       
        }

                """
        output = """Error on line 3 col 35: ,"""
        self.assertTrue(TestParser.test(input, output, 252))

    def test_253(self):
        input = """
        Class _bku_{
            Var $arr : Array[Int,3];
            foo() {
            }
        """
        output = """Error on line 6 col 8: <EOF>"""
        self.assertTrue(TestParser.test(input, output, 253))

    def test_254(self):
        input = """
            Class _bku_{
                Var $arr : Array[Int,3];
                foo() {
                    Var $a: Int;
                }    
            }
            """
        output = """Error on line 5 col 24: $a"""
        self.assertTrue(TestParser.test(input, output, 254))

    def test_255(self):
        input = """
            Class _bku_ {
                foo() {
                    Return $a;
                }
            }
        """
        output = """Error on line 4 col 27: $a"""
        self.assertTrue(TestParser.test(input, output, 255))

    def test_256(self):
        input = """
            Class Shape{
                foo(){
                    Return a::$TAloz*a::$TAloz---------a::$TAloz;
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 256))

    def test_257(self):
        input = """
            Class Shape{
                foo(){
                    Foreach (x In 1+1 .. 100+100 By a.foo()){}
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 257))

    def test_258(self):
        input = """
            Class _bku_{
                foo(){
                    Var a: Array[Int, 5],Array[Int,1];
                    a = Array(1,2,-1,3,4,5) + Array(4,3,2,1,0) == 1;
                }
            }
        """
        output = """Error on line 4 col 40: ,"""
        self.assertTrue(TestParser.test(input, output, 258))

    def test_259(self):
        input = """
                    Class Shape{
                        foo(){
                            Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                                Class Shape{}
                            }
                        }
                    }
                """
        output = """Error on line 5 col 32: Class"""
        self.assertTrue(TestParser.test(input, output, 259))

    def test_260(self):
        input = """
            Class Shape{
                foo(){
                    Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                        Var $a:Int;
                    }
                }
            }
        """
        output = """Error on line 5 col 28: $a"""
        self.assertTrue(TestParser.test(input, output, 260))

    def test_261(self):
        input = """
            Class Phuoc{
                foo(){
                    If (a > b){
                        Return 5 + 2 - 3*a + b;    
                    }
                    Elseif(b < a){
                        Continue;
                    }
                    Else{
                        Var a: Float;
                        a = 5 * 3;
                        b = New Object();
                    }
                }
            }
        """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 261))

    def test_262(self):
        input = """
                    Class Phuoc{
                        foo(){
                            If (a > b){
                                Return 5 + 2 - 3*a + b;    
                            }
                            Elseif(b < a + 5){
                                Foreach (scalar In (1+2) .. (2*3) By 5*4){
                                    Op.print("Hello world");
                                    Op::$go = 5*3 - 2;
                                }
                            }
                            Else{
                                Var a: Float;
                                a = 5 * 3;
                                b = New Object();
                                c = Shape::$getArea().square_meter;
                                Break;
                            }
                        }
                    }

                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 262))

    def test_263(self):
        input = """
                    Class Phuoc{
                        foo(){
                            If (a > b){
                                Return 5 + 2 - 3*a + b;    
                            }
                            Elseif(b < a + 5){
                                Foreach (scalar In (1+2) .. (2*3) By 5*4){
                                    Op.print("Hello world");
                                    Op::$go = 5*3 - 2;
                                }
                                b.a[0] = 5;
                            }
                            a.$c = 5;
                        }
                    }

                """
        output = """Error on line 14 col 30: $c"""
        self.assertTrue(TestParser.test(input, output, 263))

    def test_264(self):
        input = """
                    Class Phuoc{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        foo(){
                            Return a::$12abc;
                        }
                    }

                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 264))

    def test_265(self):
        input = """
                    Class Phuoc{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        foo(){
                            Return a.$12abc;
                        }
                    }

                """
        output = """Error on line 5 col 37: $12abc"""
        self.assertTrue(TestParser.test(input, output, 265))

    def test_266(self):
        input = """
                    Class Phuoc{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        foo(){
                            Return $12abc;
                        }
                    }

                """
        output = """Error on line 5 col 35: $12abc"""
        self.assertTrue(TestParser.test(input, output, 266))

    def test_267(self):
        input = """
                    Class Phuoc{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        foo($a: Int){
                            Return abc;

                            }
                }
                """
        output = """Error on line 4 col 28: $a"""
        self.assertTrue(TestParser.test(input, output, 267))

    def test_268(self):
        input = """
                    Class Phuoc{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        foo(a: Int, b: Float){
                            Return abc;
                        }
                    }

                """
        output = """Error on line 4 col 34: ,"""
        self.assertTrue(TestParser.test(input, output, 268))

    def test_269(self):
        input = """
                    Class Phuoc{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        foo(a,b: Int; c,d: Array[Int, 5]){
                            Return abc;
                        }
                    }

                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 269))

    def test_270(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            a::$b = 8;
                            Return abc;
                        }
                    }

                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 270))

    def test_271(self):
        input = """
                    Class $Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            a::$b = 8;
                            Return abc;
                        }
                    }

                """
        output = """Error on line 2 col 26: $Phuoc"""
        self.assertTrue(TestParser.test(input, output, 271))

    def test_272(self):
        input = """
                    Class Phuoc : $Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            a::$b = 8;
                            Return abc;
                        }
                    }

                """
        output = """Error on line 2 col 34: $Hello"""
        self.assertTrue(TestParser.test(input, output, 272))

    def test_273(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            a = Self.b + c;
                            Self = 8;
                        }
                    }

                """
        output = """Error on line 6 col 33: ="""
        self.assertTrue(TestParser.test(input, output, 273))

    def test_274(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            a = Self.b + c;
                            b = a[0]*a[1];
                            Return Self;
                        }
                    }

                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 274))

    def test_275(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            a = Self.b + c;
                            b = a[0]*a[1];
                            k = b[func()];
                            Return Self;
                        }
                    }

                """
        output = """Error on line 7 col 38: ("""
        self.assertTrue(TestParser.test(input, output, 275))

    def test_276(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            a = Self.b + c;
                            b = a[0]*a[1];
                            k = a.c[5].b;
                            Return Self;
                        }
                    }

                """
        output = """Error on line 7 col 38: ."""
        self.assertTrue(TestParser.test(input, output, 276))

    def test_277(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            k = a::$e.d.b.a.c[5];
                            Return Self;
                        }
                    }

                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 277))

    def test_278(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            If (a > b){
                                Return 5 + 2 - 3*a + b;    
                            }
                            Elseif(b < d::$a + 5){
                                b.a[0] = 5*4 - e + 8 / 5;

                            }
                        }
                    }

                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 278))

    def test_279(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            If (a > b){
                                Return 5 + 2 - 3*a + b;    
                            }
                            Elseif(b < d::$a + 5){
                                b.a[0] = 5*4 - e + 8 / 5 ! 4;

                            }
                        }
                    }

                """
        output = """Error on line 9 col 57: !"""
        self.assertTrue(TestParser.test(input, output, 279))

    def test_280(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            If (a > b){
                                Return 5 + 2 - 3*a + b;    
                            }
                            Elseif(b < d::$a + 5){
                                d::$c.b.a[0] = 5*4 - e + 8 / 5 + (! 4);

                            }
                        }
                    }

                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 280))

    def test_281(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            If (a > b){
                                Return 5 + 2 - 3*a + b;    
                            }
                            Elseif(b < d::$a + 5){
                                b.a[1].a[2] = 5*4 - e + 8 / 5 + (! 4);

                            }
                        }
                    }

                """
        output = """Error on line 9 col 38: ."""
        self.assertTrue(TestParser.test(input, output, 281))

    def test_282(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            If (a > b){
                                Return 5 + 2 - 3*a + b;    
                            }
                            Elseif(b < d::$a + 5){
                                os.print("Hello");
                                $c.b.a[1] = 5*4 - e + 8 / 5 + (! 4);
                            }
                        }
                    }
                """
        output = """Error on line 10 col 32: $c"""
        self.assertTrue(TestParser.test(input, output, 282))

    def test_283(self):
        input = """
                    Class Phuoc : Hello{
                        Var $12abc: Array[Array[Int, 0b1], 0x17];
                        $foo(a,b: Int; c,d: Array[Int, 5]){
                            Elseif(b < d::$a + 5){
                                os.print("Hello");
                            }
                        }
                    }

                """
        output = """Error on line 5 col 28: Elseif"""
        self.assertTrue(TestParser.test(input, output, 283))

    def test_284(self):
        input = """
                   Class People{
                        Var a, b, c: Int;
                   }
                   Class Engineer{
                       HCMUT(){
                            a = b + c * 5;
                       }

                       Constructor(){

                       }
                       Destructor(){

                       }
                   }
                   Class CSE : Engineer{
                        Class CS{
                        }
                   }
               """
        output = """Error on line 18 col 24: Class"""
        self.assertTrue(TestParser.test(input, output, 284))

    def test_285(self):
        input = """
                   Class People{
                        Var a, b, c: Int;
                   }
                   Class Engineer{
                       HCMUT(){
                            a = b + c * 5;
                            Faculty(){
                                a = b*3;
                            }
                       }
                       Constructor(){

                       }
                       Destructor(){

                       }
                   }
               """
        output = """Error on line 8 col 35: ("""
        self.assertTrue(TestParser.test(input, output, 285))

    def test_286(self):
        input = '''
            Class Program{
                main(){
                    a = "Hello world";
                    b = b +. a;
                }
            }
            function_check(){
            }
            '''
        expect = 'Error on line 8 col 12: function_check'
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = """
        Class abc{
             $homecse(){
                Var helloword: String = "ok students";
                Return $helloworld;
             }   
        }
        """
        expect = """Error on line 5 col 23: $helloworld"""
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = '''
            Class Program{
                main(){
                    a = "Hello world";
                    b = b +. a;
                    Var c: Int = 1, 5, 6;
                }
            }
            '''
        expect = 'Error on line 6 col 34: ,'
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = '''
            Class Program{
                main(){
                    a = "Hello world";
                    b = b +. a;
                    Var c,d,e: Int = 1, 5, 6;
                }
            }

            Class People{
                Engineer(c,d: Float; b::$a: Int){
                    os.print("Hello");
                }
            }
            '''
        expect = 'Error on line 11 col 38: ::'
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = """
        Class Pow{
            multi(x: Array[Int, 3] = 8; y: Float){
                manage: String = "Abc";
                os.print("Hello");
            }
        }
        """
        expect = """Error on line 3 col 35: ="""
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = """
        Class Testing{
            Var abc: Int;
            $checkCons(){
                Constructor() {
                }
            }
        }
        """
        expect = """Error on line 5 col 16: Constructor"""
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = """
        Var x, y, z: Float;
        x = 5 +4 -2;
        Class Alex{
            playgames(){
                Self.func(parafirst, parasecond, parathird);
                Var b: Boolean = 8 >= 2;
                Val val1: Boolean = True == False;
                
                a = football + Self.soccer();
                Return True;
                b = Array(1,2,3);
                Break;
            }   
        }
        """
        expect = """Error on line 2 col 8: Var"""
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = """
        Class Alex{
            playgames(){
                Self.func(param1, param2);
                Var b: Boolean = 8 >= 2;
                Val val1: Boolean = True == False;
                b = ! val1;
                a = football + Self.soccer();
                Return True;
            }   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """
            Class Pow{
                Calculate(a: Int; b: Float; c: Bool){
                    Normal(){
                        a = b*3 + 8 - 4 % 5;
                    }
                }
            }
        """
        expect = """Error on line 4 col 26: ("""
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = """
        Class Bingo{
            febr(){
                a = 1*3 + Self.febr();
                Self.febr(param1, param2);
                Val val1: Boolean = False == False != True;
                Var b: Boolean = 82 >= 3 < 5 >= 4;
                Return True;
            }
            Var a, b, c: Int = 5*3 - 2 + 4;   
        }
        """
        expect = """Error on line 6 col 51: !="""
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """
        Class think{
            Var a: Int;
            func(){
                Return Self.Circulate.n.b(a+9812).y(12+8).best.pi;
                Break;
                Return y;
            }   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = """
        Class People{
            function_check(){
                Return Self.$Circulate.n.b(a+9812).y(12+8).best.pi;
            }   
        }
        """
        expect = """Error on line 4 col 28: $Circulate"""
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = """
        Class abc{
            homecse(){
                Var helloworld: String = "ok students";
                helloworld = "New string";
            }   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = '''
            Class Program{
                main(){
                    a = "Hello world";
                    b = b +. a;
                    Var c: Program;
                }
            }
            '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        input = """
        Class moments{
            func(){
                x = hemo/human + Self.func();
                Self.func(parafirst, parasecond);
                Val test_bool: Boolean = (True == False) + 0;
                a = "Alladin";
                n = (! test_not);
                Return Self.para(42*3 + 5);
            }   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 300))
