!determine_coverage.

+!determine_coverage : req(REQ) & spec(S) <-
    .examine_coverage(S, REQ, RES);
    +covered(RES).

+!determine_coverage <- !determine_coverage.

+covered(true) <- .print("The coverage is OK").

+covered(false) <- .print("The coverage is incomplete") ; !ask_for_completion.

+req(R) <- .print ("requirements updated").

+!ask_for_completion : spec(S) & req(R) <-
    .add_req(S,R,ANSWER) ;
    -req(R);
    -covered(false);
    +req(ANSWER).

+!ask_for_completion <- +hadnoresponse.