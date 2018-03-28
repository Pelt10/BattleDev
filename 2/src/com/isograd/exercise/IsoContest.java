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

        int price = Integer.parseInt(sc.nextLine());
        sc.nextLine();

        double total = 0;
        while (sc.hasNextLine()) {
            int nbrpers = Integer.parseInt(sc.nextLine());


            double localPrice = price * nbrpers;

            if (nbrpers >= 10) {
                localPrice *= 0.7;
            } else if (nbrpers >= 6) {
                localPrice *= 0.8;
            } else if (nbrpers >= 4) {
                localPrice *= 0.9;
            }
            total += localPrice;
        }

        System.out.println((int) Math.ceil(total));
    }
}
