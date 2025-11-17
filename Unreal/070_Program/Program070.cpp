// Normal Map

#include "Program070.h"

AProgram070::AProgram070()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram070::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Normal Map ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating normal map."));

    // Implement the program logic here...
}

void AProgram070::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
