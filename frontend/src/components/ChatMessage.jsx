import ReactMarkdown from "react-markdown";

import {

    Paper,

    Typography,

    Box,

    Chip,

    Divider,

    Stack

} from "@mui/material";

import VerifiedIcon from "@mui/icons-material/Verified";
import SecurityIcon from "@mui/icons-material/Security";
import AnalyticsIcon from "@mui/icons-material/Analytics";
import DescriptionIcon from "@mui/icons-material/Description";

function ChatMessage({ message }) {

    const isUser = message.type === "user";

    const confidence = message.confidence?.confidence;

    const hallucination = message.verification?.hallucination_risk;

    const coverage = message.verification?.evidence_coverage;

    const reason = message.verification?.reason;

    return (

        <Box

            display="flex"

            justifyContent={isUser ? "flex-end" : "flex-start"}

            mb={3}

        >

            <Paper

                elevation={4}

                sx={{

                    p:3,

                    borderRadius:4,

                    width:isUser ? "70%" : "90%",

                    bgcolor:isUser ? "#1976d2" : "#ffffff",

                    color:isUser ? "#ffffff" : "#222"

                }}

            >

                <Typography

                    variant="subtitle2"

                    sx={{

                        fontWeight:"bold",

                        mb:1

                    }}

                >

                    {isUser ? "👤 You" : "🤖 Diabetes Medical Assistant"}

                </Typography>

                <ReactMarkdown>

                    {message.text}

                </ReactMarkdown>

                {

                    !isUser && (

                        <>

                            <Divider sx={{my:2}}/>

                            <Stack

                                direction="row"

                                spacing={2}

                                flexWrap="wrap"

                            >

                                <Chip

                                    icon={<VerifiedIcon/>}

                                    color="success"

                                    label={`Confidence : ${confidence}%`}

                                />

                                <Chip

                                    icon={<SecurityIcon/>}

                                    color="primary"

                                    label={`Hallucination : ${hallucination}`}

                                />

                                <Chip

                                    icon={<AnalyticsIcon/>}

                                    color="secondary"

                                    label={`Coverage : ${coverage}%`}

                                />

                            </Stack>

                            <Typography

                                sx={{

                                    mt:2,

                                    fontWeight:"bold"

                                }}

                            >

                                Verification

                            </Typography>

                            <Typography>

                                {reason}

                            </Typography>

                            <Divider sx={{my:2}}/>

                            <Typography

                                sx={{

                                    fontWeight:"bold",

                                    mb:1

                                }}

                            >

                                Sources

                            </Typography>

                            <Stack

                                spacing={1}

                            >

                                {

                                    message.sources?.map(

                                        (source,index)=>(

                                            <Chip

                                                key={index}

                                                icon={<DescriptionIcon/>}

                                                label={source}

                                                variant="outlined"

                                            />

                                        )

                                    )

                                }

                            </Stack>

                        </>

                    )

                }

            </Paper>

        </Box>

    );

}

export default ChatMessage;