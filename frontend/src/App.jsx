import {
    Box,
    Typography
} from "@mui/material";

import ChatBox from "./components/ChatBox";

import "./App.css";


function App() {

    return (

        <Box
            className="app"
        >

            <Typography

                variant="h4"

                sx={{
                    fontWeight: "bold",
                    mb: 3
                }}

            >

                🩺 Diabetes Medical Assistant

            </Typography>

            <Typography

                variant="subtitle1"

                sx={{
                    mb: 3,
                    color: "#555"
                }}

            >

                Confidence-Calibrated Hallucination-Aware RAG Framework

            </Typography>

            <ChatBox />

        </Box>

    );

}

export default App;