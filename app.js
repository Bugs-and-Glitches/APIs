const express = require('express')
const app = express()
const port = 3000

app.get('/v1/api', (req, res) => {
  res.send('Hello World!')
})

app.get('/v1/api/post', (req, res) => {
  res.send('Got a POST request')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.put('/v1/api/user', (req, res) => {
  res.send('Got a PUT request at /user')
})

app.delete('/v1/api/user', (req, res) => {
  res.send('Got a DELETE request at /user')
})

app.use('/', express.static('public'))
app.use('/public/about.html', express.static('./public/about.html'))

