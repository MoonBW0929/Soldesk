import React from 'react'
import { Link, Outlet } from 'react-router-dom'

const SiteLayout = () => {
  return (
    <>
        <table
            border={1}
            style={{
                width: 800,
                marginLeft: "auto",
                marginRight: "auto",
            }}
        >
            <tr>
                <td height={40}><h1>제목</h1></td>
            </tr>
            <tr>
                <td>
                    <Link to="/">홈</Link>&nbsp;&nbsp;
                    <Link to="/gallery.go">갤러리</Link>&nbsp;&nbsp;
                    <Link to="/notice.go">공지사항</Link>
                </td>
            </tr>
            <tr>
                <td>
                    <Outlet />
                </td>
            </tr>
        </table>
    </>
  )
}

export default SiteLayout