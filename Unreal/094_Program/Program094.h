// Client RPC
// Program 094

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program094.generated.h"

UCLASS()
class AProgram094 : public AActor
{
    GENERATED_BODY()

public:
    AProgram094();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
