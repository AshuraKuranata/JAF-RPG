const PatchNotes = () => {
  // Make a list of patch notes
  const patchNotes = [
    {
      version: "1.0.0",
      date: "11-08-2025",
      notes: "Initial Release",
    },
  ];
  
  // TO DO: Make a functional component that allows deverloper to add patch notes
  const addPatchNotes = () => {
    // Add patch notes to the list
  };

  return (
    <div className="patch-notes">
      {patchNotes.map((note) => (
        <div key={note.version}>
          <h2>{note.version}</h2>
          <p>{note.date}</p>
          <p>{note.notes}</p>
        </div>
      ))}
    </div>
  );
    
};

export default PatchNotes;