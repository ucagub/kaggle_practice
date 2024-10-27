import { useRef, useState } from "react";
// import { getSupervisedSensors} from "../../components/api";
import { Box, Divider, Grid2 as Grid, IconButton, List, ListItem, Paper, TextField} from "@mui/material";
// import MapComponent from "../../components/mapComponent/mapComponent";
// import Map as MapGl;
import SendIcon from '@mui/icons-material/Send';
import { getReply } from "../utils/api";
// import { MarkerIDMap, MarkerPoint } from "../../slices/mapSlice";

interface ReplyPayload {
  text: string
  type: string
}

const InteractiveMapPage: React.FC = () => {


  // const [markerDatas] = useState<MarkerPoint[]>([])
  // const [markerIDMap, setMarkerIDMap] = useState<MarkerIDMap | null>({});
  // const [markerIDMap, setMarkerIDMap] = useState<MarkerIDMap>(new Map<string, MarkerPoint>())
  const [chatText, setChatText] = useState<string>('')
  const [chatTextList, setChatTextList] = useState<string[]>([])
  const endOfListRef = useRef<HTMLDivElement | null>(null);
  // const [reply, setReply] = useState<ReplyPayload | null>(null)

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') { // Check if the pressed key is Enter
      handleSendMessage(); // Call the send message function
    }
  };

  const handleSendMessage = async () => {
    let newList: string[]
    if (chatText) {
      newList = [...chatTextList, chatText]
    } else {
      newList = [chatText]
    }  

    setChatTextList(newList)
    setChatText('')

    const reply: ReplyPayload = JSON.parse(await getReply(chatText))
    console.log(reply.text)

    if (reply.text) {
      newList = [...chatTextList, reply.text]
    } else {
      newList = [reply.text]
    }  

    console.log(newList)

    setChatTextList(newList)
    setChatText('')
  }

  return (
    <Grid container>
    {/* <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}> */}
      <Grid>
      {/* <Grid item xs={4}> */}
        <Paper elevation={3} >
          <Box display="flex" alignItems="center">
            <TextField
              variant="outlined"
              value={chatText}
              onChange={(e) => setChatText(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Ask me anything about air quality"
              fullWidth
            />
            <IconButton color="primary" onClick={handleSendMessage }>
              <SendIcon />
            </IconButton>
          </Box>
            
        </Paper>
      </Grid>
      <Grid>
          <List sx={{ maxHeight: 300, overflow: 'auto', width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
            {chatTextList.map((value: string, index: number) => (
              <>
              <ListItem key={index}>
                {value}
              </ListItem>
              <Divider variant="inset" component="li" sx={{ width: '80%', margin: '0 auto' }}/>
              </>
            ))}
            <div ref={endOfListRef} />
          </List>
      </Grid>

    </Grid>

  );
};

export default InteractiveMapPage;
