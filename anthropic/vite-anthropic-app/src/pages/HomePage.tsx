import Anthropic from '@anthropic-ai/sdk';
import { useEffect, useState } from 'react';
import { getReply } from '../utils/api';

interface ReplyPayload {
    text: string
    type: string
}
const HomePage: React.FC = () => {
    const apiKey = import.meta.env.VITE_ANTHROPIC_API_KEY;
    const [reply, setReply] = useState<ReplyPayload | null>(null)


    useEffect(() => {
        const fetchMessage = async () => {
            const anthropic = new Anthropic({
                apiKey: apiKey, // defaults to process.env["ANTHROPIC_API_KEY"]
            });
            const msg = await anthropic.messages.create({
                model: "claude-3-5-sonnet-20241022",
                max_tokens: 1024,
                messages: [{ role: "user", content: "Hello, Claude" }],
            });

            const reply: ReplyPayload = await getReply('How is the AQI in UP Diliman today')
            console.log(reply);
        }

        fetchMessage()

    }, [])

    return (
        <>
            Hello
        </>
    )
}

export default HomePage