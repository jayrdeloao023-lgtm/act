class Vehicle {
    String brand;

    void start() {
        System.out.println("Vehicle is starting...");
    }
}

class Car extends Vehicle {
    String model;
    String color;
    String price;
    String engine;

    void displayInfo() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Color: " + color);
        System.out.println("Price: " + price);
        System.out.println("Engine: " + engine);
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car();
        myCar.brand = "supra";
        myCar.model = "Vios";
        myCar.color = "black";
        myCar.price = "1,000,000";
        myCar.engine = "(B48)";
          
        myCar.start();
        myCar.displayInfo();
    }
}