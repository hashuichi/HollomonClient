import java.util.*;

public class CardTest {
    public static void main(String[] args){
        Set<Card> hs = new HashSet<Card>();
        Card c1 = new Card(1, "card1", Rank.COMMON, 5);
        Card c2 = new Card(1, "card1", Rank.COMMON, 10);
        Card c3 = new Card(1, "card2", Rank.UNIQUE, 5);
        Card c4 = new Card(1, "card3", Rank.RARE, 5);
        hs.add(c1);
        hs.add(c2);
        hs.add(c3);
        hs.add(c4);
        System.out.println(hs);

        Set<Card> ts = new TreeSet<Card>();
        ts.add(c1);
        ts.add(c2);
        ts.add(c3);
        ts.add(c4);
        System.out.println(ts);
    }
}