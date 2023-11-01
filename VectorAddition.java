

public class VectorAddition {

    static int[] addVectors(int[] u, int[] v) {
        // Check if the lengths of the two arrays are the same
        if (u.length != v.length) {
            throw new IllegalArgumentException("Vectors must be of the same length");
        }

        int[] result = new int[u.length];

        for (int i = 0; i < u.length; i++) {
            result[i] = u[i] + v[i];
        }

        return result;
    }

    public static void main(String[] args) {

        int [] u = new int[10];
        int [] v = new int[10];

        for (int i = 0; i < u.length; i++) {
            u[i] = (int) (Math.random() * 100);  // Generate a random number between 0 and 99
        }

        for (int i = 0; i < v.length; i++) {
            v[i] = (int) (Math.random() * 100);  // Generate a random number between 0 and 99
        }

        int[] sum = addVectors(u, v);

        System.out.print("Resulting vector: ");
        for (int value : sum) {
            System.out.print(value + " ");
        }
    }
}
