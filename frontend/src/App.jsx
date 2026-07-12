import {

    Box,

    Typography,

    Paper

} from "@mui/material";

import ChatBox from "./components/ChatBox";

import "./App.css";

function App() {

    return (

        <Box className="app">

            <Paper

                elevation={6}

                className="header"

            >

                <Typography

                    variant="h4"

                    fontWeight="bold"

                >

                    🩺 Hallucination-Aware Diabetes Medical Assistant

                </Typography>

                <Typography

                    variant="subtitle1"

                    sx={{

                        mt:1,

                        color:"#555"

                    }}

                >

                    Confidence-Calibrated Retrieval-Augmented Generation Framework

                </Typography>

                <Typography

                    variant="body2"

                    sx={{

                        mt:1,

                        color:"#777"

                    }}

                >

                    Powered by FAISS • Gemini • FastAPI • React

                </Typography>

            </Paper>

            <ChatBox/>

        </Box>

    );

}

export default App;