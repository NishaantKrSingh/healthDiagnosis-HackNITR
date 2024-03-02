
"use client"

import { useUser } from '@auth0/nextjs-auth0/client';
import savetodb from "@/actions/savetodb";
import { useState } from "react";
import { redirect } from 'next/navigation';

export default function Home() {
  const [gender, setGender] = useState('');
  const [bloodgrp, setBloodgrp] = useState('');
  const { user, error, isLoading } = useUser();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>{error.message}</div>;

  return (
    <div className="grid h-screen w-screen place-items-center bg-slate-800 px-4 text-sm font-medium">
      <div className="w-full max-w-sm rounded-lg bg-slate-700/30 shadow">
        {user ? (
          <form
            onSubmit={(e) => {
              e.preventDefault();
              savetodb({
                email: user.email,
                name: user.name,
                image: user.picture,
                gender: gender,
                bloodgrp: bloodgrp,
              })
            }}
            className="p-4 md:p-5 lg:p-6"
          >
            <div className="grid gap-y-3">
              <label htmlFor="bloodgrp" className='text-slate-200 font-semibold' >Blood Group:</label>
              <select
                id="bloodgrp"
                name="bloodgrp"
                value={bloodgrp}
                onChange={(e) => setBloodgrp(e.target.value)}
                required
                className="focus:border-purple-400 rounded-md border border-slate-600 bg-slate-700 py-3 px-4 text-slate-200 outline-none transition placeholder:text-slate-400"
              >
                <option value="" disabled selected>
                  Select your blood group
                </option>
                <option value="A+">A+</option>
                <option value="A-">A-</option>
                <option value="B+">B+</option>
                <option value="B-">B-</option>
                <option value="AB+">AB+</option>
                <option value="AB-">AB-</option>
                <option value="O+">O+</option>
                <option value="O-">O-</option>
              </select>

              <label htmlFor="gender" className='text-slate-200 font-semibold '>Gender:</label>
              <select
                id="gender"
                name="gender"
                value={gender}
                onChange={(e) => setGender(e.target.value)}
                required
                className="focus:border-purple-400 rounded-md border border-slate-600 bg-slate-700 py-3 px-4 text-slate-200 outline-none transition placeholder:text-slate-400"
              >
                <option value="" disabled selected>
                  Select your gender
                </option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
              </select>

              <button
                type="submit"
                className="flex items-center justify-center gap-x-2 rounded-md border border-slate-600 bg-slate-700 py-3 px-4 text-slate-300 transition hover:text-purple-400"
              >
                Submit
              </button>
            </div>
          </form>
        ) : (
          <a
            href="/api/auth/login"
            className="flex items-center justify-center gap-x-2 rounded-md border border-slate-600 bg-slate-700 py-3 px-4 text-slate-300 transition hover:text-purple-400"
          >
            Login
          </a>
        )}
      </div>
    </div>
  );
}
