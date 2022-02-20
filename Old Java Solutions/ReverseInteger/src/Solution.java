class Solution {
    public int reverse(int x) {
        if(x == Integer.MIN_VALUE)
            return 0;

        if(x < 0)
            x = flip(x * -1) * -1;
        else
            x = flip(x);

        return x;
    }

    private int flip(int x) {
        char[] value = Integer.toString(x).toCharArray();
        char[] store = new char[value.length];
        long check;

        for(int i = 0; i < value.length; i++) {
            store[i] = value[value.length - i - 1];
        }

        check = Long.parseLong(new String(store));

        if(check > Integer.MAX_VALUE)
            return 0;

        return (int)check;
    }
}