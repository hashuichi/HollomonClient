public class Card implements Comparable<Card> {
    private long id;
    private String name;
    private Rank rank;
    private long price;

    public Card(long id, String name, Rank rank){
        this.id = id;
        this.name = name;
        this.rank = rank;
        this.price = 0;
    }

    public Card(long id, String name, Rank rank, long price){
        this.id = id;
        this.name = name;
        this.rank = rank;
        this.price = price;
    }

    public long getID() { return this.id; }
    public String getName() {return this.name; }
    public Rank getRank() { return this.rank; }
    public long getPrice() { return this.price; }
    
    @Override
    public String toString(){
        return Long.toString(id)+" "+name+" "+rank+" "+Long.toString(price);
    }

    @Override
    public int hashCode(){
        return (int) ((id >> 32) ^ id);
    }

    @Override
    public boolean equals(Object o){
        if (!(o instanceof Card)){
            return false;
        }
        Card other = (Card) o;
        return (this.id == other.id && this.name.equals(other.name) && this.rank == other.rank);
    }

    public int compareTo(Card other){
        int rankResult = this.rank.compareTo(other.rank);
        if (rankResult == 0){
            int nameResult = this.name.compareTo(other.name);
            if (nameResult == 0){
                return Long.toString(this.id).compareTo(Long.toString(other.id));
            } else {
                return nameResult;
            }
        } else {
            return rankResult;
        }
    }
}