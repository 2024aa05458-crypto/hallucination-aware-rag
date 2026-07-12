import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

export const askQuestion = async (question) => {

    const response = await API.post("/chat", {

        question: question

    });

    return response.data;

};