/*******
 * Read input from System.in
 * Use System.out.println to ouput your result.
 * Use:
 *  IsoContestBase.localEcho( variable)
 * to display variable in a dedicated area.
 * ***/
package com.isograd.exercise;

import java.util.Scanner;

/**
 * @author pelt10
 *
 * Ce projet n'est pas terminé et ne fonctionne pas.
 */
public class IsoContest {
    public static void main(String[] argv) throws Exception {
        Scanner sc = new Scanner(System.in);
        int[] crepes = new int[6];

        int i = 0;
        while (i < 6) {
            crepes[i] = Integer.parseInt(sc.nextLine());
            i++;
        }

        System.out.println(test(crepes, -1) + 1);
    }

    // Il va vraiment falloir que je m'entraîne sur la récursivité....
    public static int test(int[] crepes, int turn) {

        if (isSort(crepes))
            return turn;
        turn++;

        int min = 8;
        for (int i = 0; i < crepes.length - turn; i++) {
            int result = test(reverse(i, crepes), turn);
            if(result < min) {
                min = result;
            }
        }

        return min;
    }

    public static boolean isSort(int[] stack) {

        for (int i = 1; i < stack.length; i++) {
            if(stack[i] < stack[i-1])
                return false;
        }

        return true;
    }

    public static int[] reverse(int i, int[] stack) {
        int[] result = stack.clone();

        for (int j = 0; j < Math.ceil(i/2.0); j++) {
            int bkp = result[j];
            result[j] = result[i-j];
            result[i-j] = bkp;
        }

        return result;
    }
}
