// Health Component
// Program 042

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program042.generated.h"

UCLASS()
class AProgram042 : public AActor
{
    GENERATED_BODY()

public:
    AProgram042();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
