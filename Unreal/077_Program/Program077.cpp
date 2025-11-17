// Sound Cue

#include "Program077.h"

AProgram077::AProgram077()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram077::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Sound Cue ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating sound cue."));

    // Implement the program logic here...
}

void AProgram077::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
