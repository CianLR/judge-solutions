
type player = {score: int; space: int}

let player_take_turn p roll =
  let new_space = (((p.space + roll) - 1) mod 10) + 1 in
  let new_score = p.score + new_space in
  {score=new_score; space=new_space}

let rec run_turn roll_stream p1 p2 =
  let r1 = Stream.next roll_stream in
  let r2 = Stream.next roll_stream in
  let r3 = Stream.next roll_stream in
  let new_p1 = player_take_turn p1 (r1 + r2 + r3) in
  if new_p1.score >= 1000 then (Stream.count roll_stream, p2.score)
  else run_turn roll_stream p2 new_p1

let () =
  let roll_stream = Stream.from (fun l -> Some ((l mod 100) + 1)) in
  let rolls, lose_score = run_turn roll_stream {score=0; space=5} {score=0; space=8} in
  Printf.printf "Rolls %d score %d. Ans %d\n" rolls lose_score (rolls * lose_score)
