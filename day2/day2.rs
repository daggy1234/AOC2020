use std::fs;
use regex::Regex;

fn readlines() -> Vec<String> {

    let text = match fs::read_to_string("day2.txt") {
        Ok(file) => file,
        Err(err) => panic!("Couldn't readlines {}", err),
    };
    let mut text_vex: Vec<String> = Vec::new();
    let lines = text.lines();
    for line in lines {
      let mystr: String = line.replace("\n","");
      text_vex.push(mystr);
    }
    text_vex
}

fn parse_data(line: &str) -> (u16,u16,&str,String) {
  let split_list = line.split(":").collect::<Vec<&str>>();
  let search = split_list[1].replace(" ","");
  let split_range = split_list[0].split(" ").collect::<Vec<&str>>();
  let chara = split_range[1];
  let sevec = split_range[0].split("-").collect::<Vec<&str>>();
  let start: u16 = sevec[0].parse().unwrap();
  let end: u16 = sevec[1].parse().unwrap();
  return (start,end,chara,search)

}


fn pword_check(tup: (u16,u16,&str,String)) -> u16{
  let query = tup.2;
  let re: Regex = Regex::new(query).unwrap();
  let vec: Vec<&str> = re.find_iter(&tup.3).map(|digits| digits.as_str()).collect();
  //println!("{}",vec.len())
  let lens = vec.len() as u16;
  //println!("{} <= {} <= {}",tup.0,lens,tup.1);
  if tup.0 <= lens && lens <= tup.1 {
    return 1
  } else {
    return 0
  }
  

}

fn pword_valid(tup: (u16,u16,&str,String)) -> u16{
  let index_a: usize = (tup.0 - 1).into();
  let index_b: usize = (tup.1 - 1).into();
  let chara = tup.3.chars().nth(index_a).unwrap();
  let charb = tup.3.chars().nth(index_b).unwrap();

  let string_char = tup.2.chars().next().unwrap();
  //println!("A: {},B;{}, Q: {}",chara,charb,string_char);
  if chara == string_char  && charb != string_char {
    return 1
  } else {
    if chara != string_char  && charb == string_char {
      return 1
    } else {
      return 0
    }
  }

}

fn main() {
  let li = readlines();
  let mut correct_count: u16 = 0;
  for line in li.iter() {
    let resp = parse_data(&line);
    correct_count = correct_count + pword_check(resp)
  };
  println!("Correct Passwords: {:?}",correct_count);

  let mut valid_count: u16 = 0;
  for line in li.iter() {
    let resp = parse_data(&line);
    valid_count = valid_count + pword_valid(resp)
  };
  println!("Valid Passwords: {:?}",valid_count);
}