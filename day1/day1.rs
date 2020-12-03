use std::fs;

fn readlines() -> Vec<u32> {

    let text = match fs::read_to_string("day1.txt") {
        Ok(file) => file,
        Err(err) => panic!("Couldn't readlines {}", err),
    };
    let mut text_vex: Vec<u32> = Vec::new();
    let lines = text.lines();
    for line in lines {
      let myint: u32 = line.parse().unwrap();
      text_vex.push(myint);
    }
    text_vex
}

fn sum_two(vecs: &Vec<u32>) -> String {
  for val in vecs.iter() {
    for subval in vecs.iter() {
      let res: u32 = 2020;
      if val + subval == res {
          return format!("Val: {}\nSubval: {}\nProduct{}",val,subval,val * subval)
      }
    }
  }
  return "Nothing".to_string()
}

fn sum_three(vecs: &Vec<u32>) -> String {
  for val in vecs.iter() {
    for subval in vecs.iter() {
      for thirdval in vecs.iter() {
        let res: u32 = 2020;
        if val + subval + thirdval == res {
            return format!("Val: {}\nSubval: {}\nThirdVal: {}\nProduct{}",val,subval,thirdval, val * subval*thirdval)
      }
    }
    }
  }
  return "Nothing".to_string()
}

fn main() {
  let li = readlines();
  let res_two = sum_two(&li);
  println!("{}",res_two);
  let res_three = sum_three(&li);
  println!("{}",res_three);
}