// Timer Handle

#include "Program029.h"

AProgram029::AProgram029()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram029::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Timer Handle ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating timer handle."));

    // Implement the program logic here...
}

void AProgram029::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
