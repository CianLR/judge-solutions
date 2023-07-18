import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;


class Dyslectionary {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        Boolean first = true;
        for (ArrayList<String> d = ReadDict(br); d != null; d = ReadDict(br)) {
            if (!first) {
                System.out.println("");
            }
            Collections.sort(d, new RevCompare());
            PrintJustified(d);
            first = false;
        }
    }

    private static ArrayList<String> ReadDict(BufferedReader br) throws IOException {
        ArrayList<String> dict = new ArrayList<String>();
        for (String s = br.readLine(); s != null; s = br.readLine()) {
            if (s.equals("")) {
                return dict;
            }
            dict.add(s);
        }
        if (!dict.isEmpty()) {
            return dict;
        }
        return null;
    }

    private static void PrintJustified(ArrayList<String> d) {
        int maxLen = 0;
        for (String s : d) {
            maxLen = Integer.max(maxLen, s.length());
        }
        String fmt = String.format("%%%ds\n", maxLen);
        for (String s : d) {
            System.out.printf(fmt, s);
        }
    }

    static class RevCompare implements Comparator<String> {
        private String reverseString(String s) {
            return (new StringBuilder(s)).reverse().toString();
        }

        @Override
        public int compare(String a, String b) {
            return reverseString(a).compareTo(reverseString(b));
        }
    }
}