import java.math.BigInteger;

interface Natural
{
    Natural zero();
    Natural succ(Natural n);
    Natural add(Natural n,Natural m); 
    Natural mult(Natural n,Natural m); 
    boolean equals(Natural n,Natural m);
}

class Decimal implements Natural {

    private static Decimal _zero = new Decimal(0);

    private BigInteger value;

    public Decimal(int i) {
        value = new BigInteger(Integer.toString(i));
    }

    @Override
    public String toString() {
        return value.toString(10);
    }

    @Override
    public Natural zero() {
        return _zero;
    }

    @Override
    public Natural succ(Natural n) {
        return null;
    }

    @Override
    public Natural add(Natural n, Natural m) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public Natural mult(Natural n, Natural m) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public boolean equals(Natural n, Natural m) {
        // TODO Auto-generated method stub
        return false;
    }
}

class Binary implements Natural {

    @Override
    public Natural zero() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public Natural succ(Natural n) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public Natural add(Natural n, Natural m) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public Natural mult(Natural n, Natural m) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public boolean equals(Natural n, Natural m) {
        // TODO Auto-generated method stub
        return false;
    }
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
    private static void validate(String message, Natural output) {
        System.out.printf("%s = %s\n", message, output.toString());
    }

    private static void DataTranslationTest() {
        Decimal d = new Decimal(42);
        validate("d", d);
    }

    public static void main(String[] args) {
        // System.out.println("Hello World!");
        DataTranslationTest();
    }
}