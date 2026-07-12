import {
    Paper,
    Typography,
    Chip,
    Box,
    Divider
} from "@mui/material";

function ChatMessage({ message }) {

    const isUser = message.type === "user";

    return (

        <Box
            display="flex"
            justifyContent={isUser ? "flex-end" : "flex-start"}
            mb={2}
        >

            <Paper
                elevation={3}
                sx={{
                    p: 2,
                    maxWidth: "80%",
                    bgcolor: isUser ? "#1976d2" : "#ffffff",
                    color: isUser ? "#ffffff" : "#000000",
                    borderRadius: 3
                }}
            >

                <Typography
                    variant="body1"
                    sx={{
                        whiteSpace: "pre-wrap"
                    }}
                >
                    {message.text}
                </Typography>

                {

                    !isUser && message.sources && (

                        <>

                            <Divider sx={{ my: 2 }} />

                            <Typography
                                variant="subtitle2"
                                gutterBottom
                            >

                                Sources

                            </Typography>

                            {

                                message.sources.map(

                                    (source, index) => (

                                        <Chip

                                            key={index}

                                            label={source}

                                            size="small"

                                            sx={{
                                                mr: 1,
                                                mb: 1
                                            }}

                                        />

                                    )

                                )

                            }

                            <Divider sx={{ my: 2 }} />

                            <Typography
                                variant="caption"
                            >

                                Confidence :

                                {" "}

                                {(message.confidence * 100).toFixed(0)}%

                            </Typography>

                        </>

                    )

                }

            </Paper>

        </Box>

    );

}

export default ChatMessage;