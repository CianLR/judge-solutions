
type player = {score: int; space: int}

let player_take_turn p roll =
  let new_space = (((p.space + roll) - 1) mod 10) + 1 in
  let new_score = p.score + new_space in
  {score=new_score; space=new_space}

let player_compare p1 p2 =
  let c = compare p1.score p2.score in
  if c != 0 then c else compare p1.space p2.space

let all_rolls =
  List.map (List.fold_left (+) 0) [
    [1; 1; 1]; [1; 1; 2]; [1; 1; 3];
    [1; 2; 1]; [1; 2; 2]; [1; 2; 3];
    [1; 3; 1]; [1; 3; 2]; [1; 3; 3];
    [2; 1; 1]; [2; 1; 2]; [2; 1; 3];
    [2; 2; 1]; [2; 2; 2]; [2; 2; 3];
    [2; 3; 1]; [2; 3; 2]; [2; 3; 3];
    [3; 1; 1]; [3; 1; 2]; [3; 1; 3];
    [3; 2; 1]; [3; 2; 2]; [3; 2; 3];
    [3; 3; 1]; [3; 3; 2]; [3; 3; 3];
  ]

let rec run_turn memo_table p1 p2 =
  let k = (p1, p2) in
  if Hashtbl.mem memo_table k then Hashtbl.find memo_table k else
  let new_p1s = List.map (player_take_turn p1) all_rolls in
  let win_games, cont_games = List.partition (fun p -> p.score >= 21) new_p1s in
  let imm_p1_wins = List.length win_games in
  let all_results = List.map (run_turn memo_table p2) cont_games in
  let sub_p2_wins, sub_p1_wins =
    List.fold_left (fun (a1, a2) (p2_w, p1_w) -> (a1 + p2_w, a2 + p1_w)) (0, 0) all_results in
  let p1_wins = sub_p1_wins + imm_p1_wins in
  Hashtbl.replace memo_table k (p1_wins, sub_p2_wins);
  (p1_wins, sub_p2_wins)

let () =
  let memo_table = Hashtbl.create (21 * 21 * 10 * 10) in
  let p1_wins, p2_wins = run_turn memo_table {score=0; space=5} {score=0; space=8} in
  Printf.printf "P1 wins %d. P2 wins %d.\n" p1_wins p2_wins 
