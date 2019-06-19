import java.util.*;

/**
 * 爬楼梯
 * 
 * f(n)=f(n-1)+f(n-1), f(0)=1 , f(1)=1
 */
public class Main {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        while (scan.hasNext()) {
            System.out.println(climbStairs(scan.nextInt()));
        }
        scan.close();
    }

    public static int climbStairs(int n) {
        double a = Math.sqrt(5);
        double b = 1.0 / 2 - a / 10;
        double c = Math.pow(1.0 / 2 - a / 2, n);
        double d = 1.0 / 2 + a / 10;
        double e = Math.pow(1.0 / 2 + a / 2, n);
        return (int) Math.round(b * c + d * e);
    }
}
