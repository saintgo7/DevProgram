// Multicast RPC
// Program 095

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program095.generated.h"

UCLASS()
class AProgram095 : public AActor
{
    GENERATED_BODY()

public:
    AProgram095();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
