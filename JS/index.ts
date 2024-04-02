const a: number = 3;

const ob: { name: string } = { name: "kim" };

type Mytype = string;

let b: Mytype = "kim";

const c: string[] = ["a", "b", "c"];

c.splice(2, 1);

console.log(c);

const man: { name?: string; pass?: boolean } = {
  name: "j",
  pass: true,
};

// const get: string | null = prompt("나이를 입력하시오");

// if (typeof get === "string") {
//   const age = parseInt(get);
//   console.log(age);
// }

const flag: boolean = true;
let cnt: number = 0;

while (flag) {
  if (cnt > 10) {
    break;
  }
  // console.log(cnt);
  cnt += 1;
}

const arr: string[] = ["첫번째", "두번째", "세번째", "네번째", "다섯번째"];

arr.map((a, i) => {
  console.log(a);
  console.log(i + 1);
  console.log("map");
});

function myFunc(x: number): void {
  return console.log(x * 10);
}

myFunc(345);

function printer(x: string, y: number): void {
  console.log(`My name is ${x}, and I'm ${y} years old`);
}

printer("kim", 22);

const add = () => {
  let a = 3;
  let b = 4;
  return a + b;
};
console.log(add());
