import React from "react";

const ConnectApi = () => {
  const apiUrl = "http://127.0.0.1:8000/api/";
  fetch(apiUrl)
    .then((reponse) => reponse.json())
    .then((data) => console.log(data));

  return <div>ConnectApi</div>;
};

export default ConnectApi;
