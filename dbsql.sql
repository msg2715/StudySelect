/* 

userid : 유저 아이디
userpw : 유저 비밀번호
username : 유저 이름
usergrade : 유저의 학년
userclass : 유저의 반
usernumber : 유저의 번호
usermail : 유저의 학교용 메일 주소

*/


CREATE TABLE user(
    userid TEXT NOT NULL UNIQUE,
    userpw TEXT NOT NULL,
    username TEXT NOT NULL,
    usergrade INTEGER NOT NULL,
    userclass INTEGER NOT NULL,
    usernumber INTEGER NOT NULL,
    usermail TEXT NOT NULL,
    choice JSON
);

/*
DROP TABLE user;
*/
