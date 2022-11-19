import java.util.*;

public class Question1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Phone number: ");
        String num = sc.nextLine();
        num = num.toUpperCase();
        System.out.print(finalNum(num));
    }

    public static String finalNum(String num) {
        long number = 0;
        int len = num.length();
        String res = "";
        for (int i = 0; i < len; i++) {
            char letter = num.charAt(i);
            if (Character.isDigit(letter)) {
                res = res + letter;
            }
            if (Character.isLetter(letter)) {
                if (letter == 'A' || letter == 'B' || letter == 'C')
                    number = 2;
                else if (letter == 'D' || letter == 'E' || letter == 'F')
                    number = 3;
                else if (letter == 'G' || letter == 'H' || letter == 'I')
                    number = 4;
                else if (letter == 'J' || letter == 'K' || letter == 'L')
                    number = 5;
                else if (letter == 'M' || letter == 'N' || letter == 'O')
                    number = 6;
                else if (letter == 'P' || letter == 'Q' || letter == 'R' || letter == 'S')
                    number = 7;
                else if (letter == 'T' || letter == 'U' || letter == 'V')
                    number = 8;
                else
                    number = 9;
                res = res + number;
            }
        }
        return res;
    }
}