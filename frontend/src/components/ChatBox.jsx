import { useState } from "react";

import {
    Box,
    TextField,
    Button,
    Paper,
    CircularProgress
} from "@mui/material";

import ChatMessage from "./ChatMessage";

import { askQuestion } from "../services/api";


function ChatBox() {

    const [messages, setMessages] = useState([]);

    const [question, setQuestion] = useState("");

    const [loading, setLoading] = useState(false);


    const sendQuestion = async () => {

        if (question.trim() === "") return;

        const userMessage = {

            type: "user",

            text: question

        };

        setMessages(prev => [...prev, userMessage]);

        setLoading(true);

        try {

            const response = await askQuestion(question);

            const botMessage = {

                type: "bot",

                text: response.answer,

                sources: response.sources,

                confidence: response.confidence,

                verification: response.verification

            };

            setMessages(prev => [...prev, botMessage]);

        }

        catch (error) {

            const botMessage = {

                type: "bot",

                text: "Unable to contact the backend."

            };

            setMessages(prev => [...prev, botMessage]);

        }

        finally {

            setLoading(false);

            setQuestion("");

        }

    };


    return (

        <Paper
            elevation={5}
            sx={{
                width: "900px",
                height: "85vh",
                display: "flex",
                flexDirection: "column",
                p: 2
            }}
        >

            <Box

                sx={{

                    flex: 1,

                    overflowY: "auto",

                    mb: 2

                }}

            >

                {

                    messages.map(

                        (message, index) => (

                            <ChatMessage

                                key={index}

                                message={message}

                            />

                        )

                    )

                }

            </Box>


            {

                loading && (

                    <Box

                        display="flex"

                        justifyContent="center"

                        mb={2}

                    >

                        <CircularProgress />

                    </Box>

                )

            }


            <Box

                display="flex"

                gap={2}

            >

                <TextField

                    fullWidth

                    label="Ask your question..."

                    value={question}

                    onChange={(e) => setQuestion(e.target.value)}

                    onKeyDown={(e) => {

                        if (e.key === "Enter") {

                            sendQuestion();

                        }

                    }}

                />

                <Button

                    variant="contained"

                    onClick={sendQuestion}

                >

                    Send

                </Button>
                <Button

                    variant="outlined"

                    color="error"

                    onClick={() => setMessages([])}

                >

                    New Chat

                </Button>

            </Box>

        </Paper>

    );

}

export default ChatBox;