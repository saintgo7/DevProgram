// Level Streaming
// Program 056

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program056.generated.h"

UCLASS()
class AProgram056 : public AActor
{
    GENERATED_BODY()

public:
    AProgram056();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
