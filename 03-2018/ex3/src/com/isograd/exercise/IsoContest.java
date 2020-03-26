/*******
 * Read input from System.in
 * Use System.out.println to ouput your result.
 * Use:
 *  IsoContestBase.localEcho( variable)
 * to display variable in a dedicated area.
 * ***/
package com.isograd.exercise;

import java.util.ArrayList;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

/**
 * @author pelt10
 *
 * Cet exercice est fonctionnel.
 */
public class IsoContest {
    public static void main(String[] argv) throws Exception {
        Scanner sc = new Scanner(System.in);

        Notes perso = new Notes(sc.nextLine());
        sc.nextLine();

        int nbrBestFriends = Integer.parseInt(sc.nextLine());

        ArrayList<Notes> friendsNotes = new ArrayList<>();

        while (sc.hasNextLine()) {
            friendsNotes.add(new Notes(sc.nextLine()));
        }

        /*
         * Le premier int correspond à la somme des différences entre notre ami et nous.
         * Le deuxième int correspond à la note du dernier film sorti.
         */
        TreeMap<Integer, Integer> friendsDiff = new TreeMap<>();

        for (Notes note : friendsNotes) {
            int totalDiff = 0;

            for (int i = 0; i < 5; i++) {
                totalDiff += diff(note.getNote(i), perso.getNote(i));
            }

            friendsDiff.put(totalDiff, note.getNote(5));
        }

        int sum = 0;
        int i = 0;
        for (Map.Entry<Integer, Integer> entry : friendsDiff.entrySet()) {
            if (i >= nbrBestFriends) {
                break;
            }
            sum += entry.getValue();
            i++;
        }
        sum /= nbrBestFriends;
        System.out.println(sum);
    }

    public static class Notes {
        int[] note = new int[6];

        public Notes(String s) {
            int i = -1;
            for (String data : s.split(" ")) {
                i++;
                note[i] = Integer.parseInt(data);
            }
        }

        public int getNote(int i) {
            return note[i];
        }
    }

    public static int diff(int a, int b) {
        return Math.abs(a - b);
    }
}
