class Vehicle {

    // Overloaded methods (Compile-Time Polymorphism)
    void info() {
        System.out.println("This is a vehicle");
    }

    void info(String brand) {
        System.out.println("Brand: " + brand);
    }

    void info(String brand, int year, String Color, String Model, String Owner, int price) {
        System.out.println("Brand: " + brand + ", Year: " + year + ", Color: " + Color +
                           ", Model: " + Model + ", Owner: " + Owner + ", Price: " + price);
    }

    // Method to be overridden
    void speed() {
        System.out.println("Vehicle has an average speed.");
    }
}

// Subclass 1
class Car extends Vehicle {
    @Override
    void speed() {
        System.out.println("Car runs at 150 km/h.");
    }
}

// Subclass 2
class Motorcycle extends Vehicle {
    @Override
    void speed() {
        System.out.println("Motorcycle runs at 120 km/h.");
    }
}

public class Main {
    public static void main(String[] args) {

        Vehicle v;

        // Using Car object
        v = new Car();
        v.info();
        v.info("Toyota");
        v.info("Toyota", 2024, "black", "Raize", "jayr", 1069000);
        v.speed();

        System.out.println();

        // Using Motorcycle object
        v = new Motorcycle();
        v.info();
        v.info("Honda");
        v.info("Honda", 2020, "white", "Click125i", "jayr", 81900);
        v.speed();
    }
}