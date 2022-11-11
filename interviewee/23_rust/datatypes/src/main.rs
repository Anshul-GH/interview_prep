fn main() {
    // scaler variables
    // integers
    let x: i32 = 2; //signed: 0 - 255 (default)
    let y: u32 = 9867; //unsigned: -127 - 128

    // float
    let a: f32 = 10.9; // (default)
    let b: f64 = 10.67;

    // bool
    // let flag: bool = 0; // only true/false values work. cannot declare 0 and 1 as bool
    let flag_2: bool = false;

    // char
    let letter: char = ';';


    // compuound types

    let tup: (i32, bool, char) = (1, true, 's');
    // cannot print tuple directly
    // println!("{}", tup)      // this wont work
    println!("{}", tup.0);
    println!("{}", tup.1);
    println!("{}", tup.2);
    println!("{:?}", tup);
    println!("{:#?}", tup);

    let mut tup2: (i32, bool, char) = (1, true, 's');
    tup2.0 = 100;

    println!("{:?}", tup2);


    // arrays
    // let arr = [1, 2, 3, 4, 5];
    let mut arr = [1, 2, 3, 4, 5];
    arr[4] = 100;
    println!("{}", arr[4]);
    println!("{:?}", arr);
}
