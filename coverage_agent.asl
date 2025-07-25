!determine_coverage.

+!determine_coverage : req(REQ) & spec(S) <-
    .external_examine_coverage(S, REQ, RES);
    +covered(RES).

+!determine_coverage <-
    !determine_coverage.

+covered(true) <-
    .print("The specification is well covered. We can stop.").

+covered(false) <-
    .print("The coverage is incomplete.") ;
     !ask_for_completion.

+req(R) <-
    .print ("Requirements updated").

+!ask_for_completion : spec(S) & req(R) <-
    .external_add_req(S,R,ANSWER) ;
    -req(R);
    -covered(false);
    +req(ANSWER) ; !determine_coverage.
