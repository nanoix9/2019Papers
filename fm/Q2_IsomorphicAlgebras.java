import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

interface Natural
{
    Natural zero();
    Natural succ(Natural n);
    Natural add(Natural n,Natural m); 
    Natural mult(Natural n,Natural m); 
    boolean equals(Natural n,Natural m);
}

class Decimal {

    private static Decimal _zero = new Decimal(BigInteger.ZERO);

    private BigInteger value;

    public Decimal(String s) {
        this(new BigInteger(s));
    }

    public Decimal(BigInteger i) {
        value = i;
    }

    @Override
    public String toString() {
        return value.toString(10);
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        };

        if (!(other instanceof Decimal)) {
            return false;
        }

        return equals(this, (Decimal)other);
    }

    public String toBinaryString() {
        return value.toString(2);
    }

    public static Decimal zero() {
        return _zero;
    }

    public static Decimal succ(Decimal n) {
        return new Decimal(n.value.add(BigInteger.ONE));
    }

    public static Decimal add(Decimal n, Decimal m) {
        return new Decimal(n.value.add(m.value));
    }

    public static Decimal mult(Decimal n, Decimal m) {
        return new Decimal(n.value.multiply(m.value));
    }

    public static boolean equals(Decimal n, Decimal m) {
        return n.value.equals(m.value);
    }
}

class Binary {

    private static Binary _zero = new Binary("0");
    private static Binary _one = new Binary("1");

    private List<Integer> value;

    /**
     * The bits are stored with most significant bits at largest index
     * @param bits
     */
    private Binary(List<Integer> bits) {
        value = bits;
    }

    public Binary(String s) throws RuntimeException {
        int i = 0;
        int start = 0;
        List<Integer> lst = new ArrayList<Integer>();
        
        // trim leading 0s
        if (s.length() > 1) {
            while (s.charAt(start) != '1') {
                start++;
            }
        }

        i = s.length() - 1;
        while (i >= start) {
            char c = s.charAt(i);
            if (c == '0') {
                lst.add(0);
            } else if (c == '1') {
                lst.add(1);
            } else {
                throw new RuntimeException("not a binary number: " + s);
            }
            i--;
        }

        value = lst;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = value.size() - 1; i >= 0; i--) {
            sb.append(value.get(i));
        }
        // sb.append('b');
        return sb.toString();
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        };

        if (!(other instanceof Binary)) {
            return false;
        }

        return equals(this, (Binary)other);
    }

    @Override
    public Binary clone() {
        return new Binary(new ArrayList<Integer>(value));
    }

    List<Integer> bitArray() {
        return value;
    }

    /* add another binary number into its own in an inplace manner 
     * a left shift can be applied to the number to add
     */
    private void inplaceAdd(Binary n, int lshift) {
        int nLen = n.value.size() + lshift;
        int carry = 0;
        int i = 0;
        for (i = 0; i < Math.min(value.size(), nLen); i++) {
            int a = value.get(i);
            int b = i < lshift ? 0 : n.value.get(i - lshift);
            int sum = a + b + carry;
            if (sum < 2) {
                value.set(i, sum);
                carry = 0;
            } else {
                value.set(i, sum - 2);
                carry = 1;
            }
        }

        /* only one of the two following for-loop will be executed */
        for (; i < nLen; i++) {
            int b = i < lshift ? 0 : n.value.get(i - lshift);
            int sum = b + carry;
            if (sum < 2) {
                value.add(sum);
                carry = 0;
            } else {
                value.add(sum - 2);
                carry = 1;
            }
        }

        for (; i < value.size(); i++) {
            int sum = value.get(i) + carry;
            if (sum < 2) {
                value.set(i, sum);
                carry = 0;
            } else {
                value.set(i, sum - 2);
                carry = 1;
            }
        }

        if (carry > 0) {
            value.add(carry);
        }
    }

    private void inplaceAdd(Binary n) {
        inplaceAdd(n, 0);
    }

    public static Binary zero() {
        return _zero;
    }

    public static Binary succ(Binary n) {
        Binary ret = n.clone();
        ret.inplaceAdd(_one);
        return ret;
    }

    public static Binary add(Binary n, Binary m) {
        Binary ret = n.clone();
        ret.inplaceAdd(m);
        return ret;
    }

    public static Binary mult(Binary n, Binary m) {
        Binary ret = _zero.clone();
        for (int i = 0; i < n.value.size(); i++) {
            if (n.value.get(i) == 1) {
                System.out.printf("%d: %s + %s", i, ret, m);
                ret.inplaceAdd(m, i);
                System.out.printf(" = %s\n", ret);
            }
        }
        return ret;
    }

    public static boolean equals(Binary n, Binary m) {
        if (n.value.size() != m.value.size()) {
            return false;
        }

        for (int i = 0; i < n.value.size(); i++) {
            if (n.value.get(i) != m.value.get(i)) {
                return false;
            }
        }

        return true;
    }
}

class NaturalConversion {
    /**
     * returns the Binary equivalence of Decimal number d
     * @param d
     * @return
     */
    public static Binary alpha(Decimal d) {
        return new Binary(d.toBinaryString());
    }

    /**
     * returns the Decimal equivalence of Binary number b
     * @param b
     * @return
     */
    public static Decimal beta(Binary bin) {
        return new Decimal(new BigInteger(bin.toString(), 2));
    }
}

public class Q2_IsomorphicAlgebras
{
    private static Random random = new Random();

    private static void validate(String message, Object output) {
        System.out.printf("%s = %s\n", message, output.toString());
    }

    private static void DataTranslationTest1() {
        Decimal d = new Decimal("42");
        Binary b = new Binary("1011");
        validate("d", d);
        validate("42 + 10", Decimal.add(d, new Decimal("10")));
        validate("42 * 10", Decimal.mult(d, new Decimal("10")));

        validate("b", b);
        Binary bn = b;
        for (int i = 0; i < 20; i++) {
            bn = Binary.succ(bn);
            // validate("next " + i, bn);
            System.out.printf("bin %s -> dec %s\n", bn, NaturalConversion.beta(bn));
        }

        // validate("sum " + b + " " + bn, Binary.add(b, bn));
        // validate("sum " + b + " 101b", Binary.mult(b, new Binary("101")));
        // validate("sum " + b + " 1101b", Binary.mult(b, new Binary("1101")));
        // validate("sum " + b + " 11111b", Binary.mult(b, new Binary("11111")));
        // validate("mul 101b " + b, Binary.mult(new Binary("101"), b));
        // validate("mul 1101b " + b, Binary.mult(new Binary("1101"), b));
        // validate("mul 11111b " + b, Binary.mult(new Binary("11111"), b));

    }

    private static void validate(String leftMsg, String rightMsg, 
            Object leftResult, Object rightResult) {
        System.out.printf("[%s] " + leftMsg + " = " + rightMsg + "\n", 
                leftResult.equals(rightResult) ? "OK" : "FAILED!");
        System.out.printf("\tLHS: " + leftMsg + " = %s\n", leftResult);
        System.out.printf("\tRHS: " + rightMsg + " = %s\n", rightResult);
        // System.out.println(output);
        // System.out.println(expected);
        // System.out.println(output.equals(expected));
        // System.out.println(output.equals(output));
    }

    private static void validate(String leftMsg, String rightMsg, 
            Object leftParam, Object rightParam, 
            Object leftResult, Object rightResult) {
        System.out.printf("[%s] " + leftMsg + " = " + rightMsg + "\n", 
                leftResult.equals(rightResult) ? "OK" : "FAILED!",
                leftParam, rightParam);
        System.out.printf("\tLHS: " + leftMsg + " = %s\n", leftParam, leftResult);
        System.out.printf("\tRHS: " + rightMsg + " = %s\n", rightParam, rightResult);
        // System.out.println(output);
        // System.out.println(expected);
        // System.out.println(output.equals(expected));
        // System.out.println(output.equals(output));
    }

    private static void validate(String leftMsg, String rightMsg, 
            Object leftParam1, Object leftParam2, Object rightParam1, Object rightParam2, 
            Object leftResult, Object rightResult) {
        System.out.printf("[%s] " + leftMsg + " = " + rightMsg + "\n", 
                leftResult.equals(rightResult) ? "OK" : "FAILED!",
                leftParam1, leftParam2, rightParam1, rightParam2);
        System.out.printf("\tLHS: " + leftMsg + " = %s\n", leftParam1, leftParam2, leftResult);
        System.out.printf("\tRHS: " + rightMsg + " = %s\n", rightParam1, leftParam2, rightResult);
        // System.out.println(output);
        // System.out.println(expected);
        // System.out.println(output.equals(expected));
        // System.out.println(output.equals(output));
    }

    private static void TestTransDec2Bin(Decimal d) {
        validate("beta(alpha(%s))", "%s", d, d, NaturalConversion.beta(NaturalConversion.alpha(d)), d);
    }

    private static void TestTransBin2Dec(Binary b) {
        validate("alpha(beta(%s))", "%s", b, b, NaturalConversion.alpha(NaturalConversion.beta(b)), b);
    }

    private static void DataTranslationTest() {
        System.out.println("============== Data Translation Test ==============");
        // TestTransDec2Bin("5453");
        TestTransDec2Bin(randomDecimal());
        TestTransBin2Dec(randomBinary());
    }

    private static void OperationDec2BinTest() {
        Decimal n = randomDecimal();
        Decimal m = randomDecimal();

        System.out.println("======== Operation Test: Decimal -> Binary ========");
        validate("alpha(zero())", "zero()", NaturalConversion.alpha(Decimal.zero()), Binary.zero());
        validate("alpha(succ(%s))", "succ(alpha(%s))", n, n, 
                NaturalConversion.alpha(Decimal.succ(n)), 
                Binary.succ(NaturalConversion.alpha(n)));
        validate("alpha(add(%s,%s))", "add(alpha(%s),alpha(%s))", n, m, n, m,
                NaturalConversion.alpha(Decimal.add(n, m)), 
                Binary.add(NaturalConversion.alpha(n), NaturalConversion.alpha(m)));
        validate("alpha(mult(%s,%s))", "mult(alpha(%s),alpha(%s))", n, m, n, m,
                NaturalConversion.alpha(Decimal.mult(n, m)), 
                Binary.mult(NaturalConversion.alpha(n), NaturalConversion.alpha(m)));
        validate("equals(%s,%s)", "equals(alpha(%s),alpha(%s))", n, m, n, m,
                Decimal.equals(n, m), 
                Binary.equals(NaturalConversion.alpha(n), NaturalConversion.alpha(m)));
        m = n;
        validate("equals(%s,%s)", "equals(alpha(%s),alpha(%s))", n, m, n, m,
                Decimal.equals(n, m), 
                Binary.equals(NaturalConversion.alpha(n), NaturalConversion.alpha(m)));
    }

    private static void OperationBin2DecTest() {
        Binary n = randomBinary();
        Binary m = randomBinary();

        System.out.println("======== Operation Test: Binary -> Decimal ========");
        validate("beta(zero())", "zero()", NaturalConversion.beta(Binary.zero()), Decimal.zero());
        validate("beta(succ(%s))", "succ(beta(%s))", n, n,
                NaturalConversion.beta(Binary.succ(n)),
                Decimal.succ(NaturalConversion.beta(n)));
        validate("beta(add(%s,%s))", "add(beta(%s),beta(%s))", n, m, n, m,
                NaturalConversion.beta(Binary.add(n, m)),
                Decimal.add(NaturalConversion.beta(n), NaturalConversion.beta(m)));
        validate("beta(mult(%s,%s))", "mult(beta(%s),beta(%s))", n, m, n, m,
                NaturalConversion.beta(Binary.mult(n, m)),
                Decimal.mult(NaturalConversion.beta(n), NaturalConversion.beta(m)));
        validate("equals(%s,%s)", "equals(beta(%s),beta(%s))", n, m, n, m,
                Binary.equals(n, m),
                Decimal.equals(NaturalConversion.beta(n), NaturalConversion.beta(m)));
        m = n;
        validate("equals(%s,%s)", "equals(beta(%s),beta(%s))", n, m, n, m,
                Binary.equals(n, m),
                Decimal.equals(NaturalConversion.beta(n), NaturalConversion.beta(m)));
    }

    private static Decimal randomDecimal() {
        return new Decimal(new BigInteger(10, random));
    }

    private static Binary randomBinary() {
        return new Binary(new BigInteger(10, random).toString(2));
    }

    public static void main(String[] args) {
        boolean timeSeed = true;
        if (timeSeed) {
            System.out.println("Randomise by using time as the seed of random generator");
            random.setSeed(System.currentTimeMillis());
        } else {
            System.out.println("The seed of random generator is fixed");
        }

        DataTranslationTest();
        OperationDec2BinTest();
        OperationBin2DecTest();
    }
}