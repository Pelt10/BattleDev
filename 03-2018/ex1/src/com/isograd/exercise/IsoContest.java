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
 * Cet exercice est fonctionnel.
 */
public class IsoContest {
    public static void main(String[] argv) throws Exception {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();

        int max = -1;
        while (sc.hasNextLine()) {
            int sum = 0;
            for (String integer : sc.nextLine().split(" ")) {
                sum += Integer.parseInt(integer);
            }

            sum = (int) Math.ceil(sum / 3.0);

            if (sum > max)
                max = sum;

        }
        System.out.println(max);
    }
}
