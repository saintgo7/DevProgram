// Server RPC
// Program 093

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program093.generated.h"

UCLASS()
class AProgram093 : public AActor
{
    GENERATED_BODY()

public:
    AProgram093();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
