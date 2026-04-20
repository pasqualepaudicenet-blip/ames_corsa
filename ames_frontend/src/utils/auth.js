import axios from "axios";

export async function verifyToken(token) {
  try {
    await axios.post("http://127.0.0.1:8000/api/token/verify/", {
      token: token,
    });
    console.log('okok')
    return true; // valido
  } catch (e) {
    console.log(e)
    return false; // non valido
  }
}