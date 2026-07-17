import { ReactNode } from "react";

import AppHeader from "./AppHeader";
import AppSidebar from "./AppSidebar";

interface AppLayoutProps {
  children: ReactNode;
}

export default function AppLayout({ children }: AppLayoutProps) {
  return (
    <div className="flex min-h-screen bg-slate-100">
      <AppSidebar />

      <div className="flex flex-1 flex-col">
        <AppHeader />

        <main className="flex-1 overflow-auto p-6">
          {children}
        </main>
      </div>
    </div>
  );
}