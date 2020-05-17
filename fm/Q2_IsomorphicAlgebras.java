import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
        List<Integer> lst = new ArrayList<Integer>();
        
        // trim leading 0s
        if (s.length() > 1) {
            while (s.charAt(i) != '1') {
                i++;
            }
        }

        while (i < s.length()) {
            char c = s.charAt(i);
            if (c == '0') {
                lst.add(0);
            } else if (c == '1') {
                lst.add(1);
            } else {
                throw new RuntimeException("not a binary number: " + s);
            }
            i++;
        }

        value = lst;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = value.size() - 1; i >= 0; i--) {
            sb.append(value.get(i));
        }
        sb.append('b');
        return sb.toString();
    }

    public static Binary zero() {
        return _zero;
    }

    public static Binary succ(Binary n) {
        List<Integer> ns = new ArrayList<Integer>();

        int carry = 1;
        for (int i: n.value) {
            // System.out.println(i);
            int sum = i + carry;
            if (sum < 2) {
                ns.add(sum);
                carry = 0;
            } else {
                ns.add(sum - 2);
                carry = 1;
            }
        }

        if (carry > 0) {
            ns.add(carry);
        }

        return new Binary(ns);
    }

    public static Binary add(Binary n, Binary m) {
        List<Integer> ns = new ArrayList<Integer>();

        int carry = 0;
        for (int i = 0; i < Math.max(n.value.size(), m.value.size()); i++) {
            int a = i < n.value.size() ? n.value.get(i) : 0;
            int b = i < m.value.size() ? m.value.get(i) : 0;
            int sum = a + b + carry;
            if (sum < 2) {
                ns.add(sum);
                carry = 0;
            } else {
                ns.add(sum - 2);
                carry = 1;
            }
        }

        if (carry > 0) {
            ns.add(carry);
        }

        return new Binary(ns);
    }

    public static Binary mult(Binary n, Binary m) {
        // TODO Auto-generated method stub
        return null;
    }

    public static boolean equals(Binary n, Binary m) {
        // TODO Auto-generated method stub
        return false;
    }

    // private static int[] list2array(List<Integer> lst) {
    //     int [] a = new int[lst.size()];
    //     for (int i = 0; i < lst.size(); i++) {
    //         a[i] = lst.get(i);
    //     }
    //     System.out.println("-----");
    //     System.out.println(lst);
    //     System.out.println(Arrays.asList(a));
    //     return a;
    // }
}

class NaturalConversion {
    /**
     * returns the Binary equivalence of Decimal number d
     * @param d
     * @return
     */
    public static Binary alpha(Decimal d) {
        return null;
    }

    /**
     * returns the Decimal equivalence of Binary number b
     * @param b
     * @return
     */
    public static Decimal beta(Binary b) {
        return null;
    }
}

public class Q2_IsomorphicAlgebras
{
    private static void validate(String message, Object output) {
        System.out.printf("%s = %s\n", message, output.toString());
    }

    private static void DataTranslationTest() {
        Decimal d = new Decimal("42");
        Binary b = new Binary("1001");
        validate("d", d);
        validate("42 + 10", Decimal.add(d, new Decimal("10")));
        validate("42 * 10", Decimal.mult(d, new Decimal("10")));

        validate("b", b);
        Binary bn = b;
        for (int i = 0; i < 1; i++) {
            bn = Binary.succ(bn);
            validate("next " + i, bn);
        }

        validate("sum " + b + " " + bn, Binary.add(b, bn));
        validate("sum " + b + " 101b", Binary.add(b, new Binary("101")));
        validate("sum " + b + " 1101b", Binary.add(b, new Binary("1101")));
        validate("sum " + b + " 11111b", Binary.add(b, new Binary("11111")));

    }

    public static void main(String[] args) {
        // System.out.println("Hello World!");
        DataTranslationTest();
    }
}